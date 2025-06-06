# EEP25-Sumitup

A project for EEP Summer 2025 - Web app for newsletters summary

## What

    - A full-stack web app that ingests popular tech newsletters, strips the noise, summaries them with Google Gemini, and serves a clean dashboard.

## How

    Stack
    - Frontend: Astro + React with Shadcn UI
    - Backend: Python FastAPI (uv as package manager)
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
