## Backend for sumitup project

This is the backend for the sumitup AI Newsletter summary web app.

Backend stack

- FastAPI
- Google gemini genai
- Motor for mongodb async

## How to run backend

- This project use uv as the main python package manager. To install uv please follow the guide found at https://docs.astral.sh/uv/getting-started/installation/

1. Make sure uv is installed
2. Run `uv sync --lock` - Installs or updates your environment strictly according to the existing uv.lock file, without updating or regenerating the lockfile.
3. Run `uv run  main.py`
