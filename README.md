# EEP25-Sumitup

```md
  .              +   .                .   . .     .  .
                   .                    .       .     *
  .       *                        . . . .  .   .  + .
            "You Are Here"            .   .  +  . . .
.                 |             .  .   .    .    . .
                  |           .     .     . +.    +  .
                  |             .       .   . .
        . .       V          .    * . . .  .  +   .
           +      .           .   .      +
                            .       . +  .+. .
  .                      .     . + .  . .     .      .
           .      .    .     . .   . . .        ! /
      *             .    . .  +    .  .       - O -
          .     .    .  +   . .  *  .       . / |
               . + .  .  .  .. +  .
.      .  .  .  *   .  *  . +..  .            *
 .      .   . .   .   .   . .  +   .    .            +
```

A project for EEP Summer 2025 - Digital Newsletter Garden ([web client](https://sumitup.dev/) - [source](https://github.com/polskiTran/Sumitup-quartz-dev); [Agent Assistant](https://github.com/polskiTran/EEP25-Sumitup-Agent-Assistant))

## What

    - A full-stack web app that ingests popular tech newsletters, strips the noise with Google Gemini, and serves a clean dashboard along side an Agentic AI Assistant.

## How

    Stack
    - Frontend: Quartz V4
    - Backend: Python FastAPI + Pydantic
    - LLM: gemini-2.0-flash, few-shot prompt, JSON-only output
    - Database: MongoDB Atlas, optional Atlas Vector Search for semantic queries
    - Email integration: GmailAPI

## Why

    - Cause no one like reading 10+ newsletter every morning in their inbox

## Development Setup

The backend uses [`uv`](https://docs.astral.sh/uv/) to manage Python
dependencies. After installing `uv`, install the locked dependencies and
run the server with:

    ```bash
    cd backend
    uv sync --lock
    uv run main.py
    ```
