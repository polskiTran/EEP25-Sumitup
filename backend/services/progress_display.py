"""Rich-based progress display for the newsletter fetch-and-process pipeline.

Provides a live terminal UI with per-newsletter progress bars, stage
indicators, and highlighted error/retry messages.
"""

import contextvars
import logging
from enum import Enum

from rich.console import Console, Group
from rich.live import Live
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
)
from rich.text import Text

# ---------------------------------------------------------------------------
# Context variables – allow genai_service (deep in the call stack) to report
# retry / error events back to the tracker without explicit parameter threading.
# ---------------------------------------------------------------------------
_current_tracker: contextvars.ContextVar["PipelineProgressTracker | None"] = (
    contextvars.ContextVar("_current_tracker", default=None)
)
_current_newsletter_ctx: contextvars.ContextVar["NewsletterContext | None"] = (
    contextvars.ContextVar("_current_newsletter_ctx", default=None)
)


def get_current_tracker() -> "PipelineProgressTracker | None":
    """Return the active tracker (if any) from the current async context."""
    return _current_tracker.get()


def get_current_newsletter_ctx() -> "NewsletterContext | None":
    """Return the active newsletter context (if any)."""
    return _current_newsletter_ctx.get()


def set_newsletter_ctx(ctx: "NewsletterContext | None") -> contextvars.Token:
    """Set the newsletter context for the current async task."""
    return _current_newsletter_ctx.set(ctx)


# ---------------------------------------------------------------------------
# Stage enum
# ---------------------------------------------------------------------------
class Stage(Enum):
    """Processing stages for a single newsletter.

    Each member is ``(ordinal, label)``.  *ordinal* drives the progress bar
    percentage (``ordinal / TOTAL_STAGES``).
    """

    QUEUED = (0, "Queued")
    FETCHING = (1, "Fetching")
    DEDUP_CHECK = (2, "Checking duplicates")
    HTML_TO_MD = (3, "HTML -> Markdown")
    LLM_CLEANUP = (4, "LLM Cleanup")
    EMBEDDING = (5, "Embedding")
    SAVE_DB = (6, "Saving to DB")
    COMPLETE = (7, "Complete")
    SKIPPED = (7, "Skipped (duplicate)")
    FAILED = (-1, "Failed")

    @property
    def ordinal(self) -> int:
        return self.value[0]

    @property
    def label(self) -> str:
        return self.value[1]


TOTAL_STAGES = 7  # fetching(1) … save_db(6) → 7 steps to reach COMPLETE


# ---------------------------------------------------------------------------
# Lightweight context carrier for newsletter identity
# ---------------------------------------------------------------------------
class NewsletterContext:
    """Carries the newsletter id + human-readable label through context vars."""

    __slots__ = ("newsletter_id", "label")

    def __init__(self, newsletter_id: str, label: str = "") -> None:
        self.newsletter_id = newsletter_id
        self.label = label


# ---------------------------------------------------------------------------
# Stage style helpers
# ---------------------------------------------------------------------------
_STAGE_STYLES: dict[Stage, str] = {
    Stage.QUEUED: "dim",
    Stage.FETCHING: "cyan",
    Stage.DEDUP_CHECK: "cyan",
    Stage.HTML_TO_MD: "cyan",
    Stage.LLM_CLEANUP: "blue",
    Stage.EMBEDDING: "magenta",
    Stage.SAVE_DB: "cyan",
    Stage.COMPLETE: "bold green",
    Stage.SKIPPED: "yellow",
    Stage.FAILED: "bold red",
}


def _styled_stage(stage: Stage, detail: str = "") -> Text:
    """Return a Rich Text with the stage label in its colour."""
    style = _STAGE_STYLES.get(stage, "")
    text = stage.label
    if detail:
        text = f"{text} ({detail})"
    return Text(text, style=style)


# ---------------------------------------------------------------------------
# Logging suppression – blocks all log records from reaching StreamHandlers
# while the Rich Live display is active, preventing them from corrupting
# the in-place refresh.
# ---------------------------------------------------------------------------
class _SuppressFilter(logging.Filter):
    """Filter that rejects every record, effectively muting a handler."""

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: ARG002
        return False


# ---------------------------------------------------------------------------
# PipelineProgressTracker
# ---------------------------------------------------------------------------
class PipelineProgressTracker:
    """Async context manager that drives a Rich live progress display.

    Uses a single ``rich.live.Live`` context that renders both the overall
    progress bar and per-newsletter progress bars together, avoiding the
    display conflicts that would arise from two independent ``Progress.start()``
    calls.

    Usage::

        async with PipelineProgressTracker(total=15, max_concurrent=5) as tracker:
            tracker.add_newsletter("abc123", "Newsletter 1")
            tracker.update_stage("abc123", Stage.FETCHING)
            ...
    """

    def __init__(self, total_newsletters: int, max_concurrent: int) -> None:
        self.total = total_newsletters
        self.max_concurrent = max_concurrent
        self.console = Console()

        # Overall progress bar (top row) — used as a renderable, NOT started
        self._overall_progress = Progress(
            TextColumn("[bold]Sumitup Pipeline[/bold]"),
            BarColumn(bar_width=40),
            MofNCompleteColumn(),
            TextColumn("processed"),
            TimeElapsedColumn(),
        )

        # Per-newsletter progress bars — used as a renderable, NOT started
        self._newsletter_progress = Progress(
            TextColumn("  {task.fields[index]:>3}"),
            TextColumn("{task.fields[sender]:<20}"),
            BarColumn(bar_width=30),
            TextColumn("{task.percentage:>5.0f}%"),
            TextColumn("{task.fields[stage_text]}"),
            TimeElapsedColumn(),
        )

        self._overall_task: TaskID | None = None
        self._tasks: dict[str, TaskID] = {}  # newsletter_id → TaskID
        self._live: Live | None = None
        self._token: contextvars.Token | None = None

        # Logging suppression state
        self._suppress_filter = _SuppressFilter()
        self._suppressed_handlers: list[logging.Handler] = []

    # -- async context manager ----------------------------------------------

    async def __aenter__(self) -> "PipelineProgressTracker":
        # Suppress all logging StreamHandlers so their output doesn't
        # break the Rich Live in-place refresh.
        self._suppress_logging()

        self._overall_task = self._overall_progress.add_task(
            "overall", total=self.total
        )
        # Combine both progress widgets into a single live renderable
        self._live = Live(
            Group(self._overall_progress, self._newsletter_progress),
            console=self.console,
            refresh_per_second=10,
        )
        self._live.start()
        self._token = _current_tracker.set(self)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:  # noqa: ANN001
        if self._live is not None:
            self._live.stop()
            self._live = None
        if self._token is not None:
            _current_tracker.reset(self._token)
            self._token = None

        # Restore logging handlers
        self._restore_logging()
        return False

    # -- public API ---------------------------------------------------------

    def add_newsletter(self, newsletter_id: str, label: str, index: int) -> None:
        """Register a newsletter as *Queued* in the display."""
        task_id = self._newsletter_progress.add_task(
            newsletter_id,
            total=TOTAL_STAGES,
            completed=0,
            sender=label,
            index=index,
            stage_text=_styled_stage(Stage.QUEUED),
        )
        self._tasks[newsletter_id] = task_id

    def update_stage(
        self, newsletter_id: str, stage: Stage, detail: str = ""
    ) -> None:
        """Advance a newsletter to *stage* and update its display row."""
        task_id = self._tasks.get(newsletter_id)
        if task_id is None:
            return
        completed = max(stage.ordinal, 0)
        self._newsletter_progress.update(
            task_id,
            completed=completed,
            stage_text=_styled_stage(stage, detail),
        )

    def update_sender(self, newsletter_id: str, sender: str) -> None:
        """Update the sender/label column after fetching the message."""
        task_id = self._tasks.get(newsletter_id)
        if task_id is None:
            return
        self._newsletter_progress.update(task_id, sender=sender)

    def mark_complete(self, newsletter_id: str) -> None:
        """Mark a newsletter as successfully completed."""
        self.update_stage(newsletter_id, Stage.COMPLETE)
        self._advance_overall()

    def mark_skipped(self, newsletter_id: str) -> None:
        """Mark a newsletter as skipped (duplicate)."""
        self.update_stage(newsletter_id, Stage.SKIPPED)
        self._advance_overall()

    def mark_failed(self, newsletter_id: str, error: str) -> None:
        """Mark a newsletter as failed and log the error."""
        self.update_stage(newsletter_id, Stage.FAILED)
        task_id = self._tasks.get(newsletter_id)
        sender = ""
        if task_id is not None:
            task = self._newsletter_progress._tasks.get(task_id)  # noqa: SLF001
            if task is not None:
                sender = task.fields.get("sender", "")
        self.log_error(newsletter_id, sender, error)
        self._advance_overall()

    # -- logging helpers (print above the live bars) ------------------------

    def log_retry(
        self,
        newsletter_id: str,
        label: str,
        attempt: int,
        max_attempts: int,
        reason: str,
        wait_seconds: float,
    ) -> None:
        """Log a retry warning above the progress bars."""
        self.console.log(
            f"[yellow]WARNING[/yellow]  "
            f"Newsletter {label or newsletter_id}: "
            f"Retry {attempt}/{max_attempts} "
            f"({reason}), waiting {wait_seconds:.1f}s"
        )

    def log_error(self, newsletter_id: str, label: str, error: str) -> None:
        """Log an error message above the progress bars."""
        self.console.log(
            f"[bold red]ERROR[/bold red]    "
            f"Newsletter {label or newsletter_id}: {error}"
        )

    def log_info(self, message: str) -> None:
        """Log a general info message above the progress bars."""
        self.console.log(f"[blue]INFO[/blue]     {message}")

    # -- internals ----------------------------------------------------------

    def _advance_overall(self) -> None:
        """Bump the overall progress bar by one."""
        if self._overall_task is not None:
            self._overall_progress.advance(self._overall_task, 1)

    def _suppress_logging(self) -> None:
        """Add a reject-all filter to every ``StreamHandler`` across all loggers.

        This prevents plain-text log output from being interleaved with the
        Rich Live display, which would cause the progress bars to scroll
        instead of refreshing in place.
        """
        self._suppressed_handlers.clear()
        # Walk the root logger + every named logger registered so far
        all_loggers: list[logging.Logger] = [logging.getLogger()]  # root
        for name in list(logging.Logger.manager.loggerDict):
            obj = logging.Logger.manager.loggerDict[name]
            if isinstance(obj, logging.Logger):
                all_loggers.append(obj)

        for log in all_loggers:
            for handler in log.handlers:
                if isinstance(handler, logging.StreamHandler):
                    handler.addFilter(self._suppress_filter)
                    self._suppressed_handlers.append(handler)

    def _restore_logging(self) -> None:
        """Remove the reject-all filter, restoring normal logging output."""
        for handler in self._suppressed_handlers:
            handler.removeFilter(self._suppress_filter)
        self._suppressed_handlers.clear()
