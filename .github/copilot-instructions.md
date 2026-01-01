# AI Coding Agent Instructions - Mario Kart World Track Randomizer

## Project Overview
This is a Python project (3.13+) for randomizing Mario Kart World tracks. Currently in early stages with minimal implementation. The project uses uv and pyproject.toml for dependency management.

## Key Architecture Patterns

### Project Structure
- **`main.py`**: Entry point for the application (single file bootstrap currently)
- **`pyproject.toml`**: Dependency and metadata management (uv)
- **`README.md`**: Project documentation (currently empty)
- No external dependencies yet; keep this minimal until required

### Python Version & Environment
- Requires Python 3.13+
- Use `.python-version` file to specify the Python version
- uv handles virtual environment and dependencies via `pyproject.toml`

## Development Workflow

### Running the Project
```bash
uv run python main.py
```

### Adding Dependencies
- Use `uv add <package>` to add dependencies (updates `pyproject.toml` automatically)
- Update the `requires-python` constraint in `pyproject.toml` if needed
- uv generates `uv.lock` for reproducible builds

## Code Organization Conventions

### Current Stage
- Single `main.py` file serves as entry point
- When expanding, follow this structure:
  - `main.py` — CLI/application entry point only
  - `src/randomizer/` — Core randomization logic (once substantial)
  - `src/models/` — Data models for tracks, cups, etc.
  - `tests/` — Unit tests (add pytest once testing is needed)

### Naming & Patterns
- Use snake_case for module and function names
- Use PascalCase for class names
- Keep functions focused and testable (relevant once scope grows)

## Integration Points & Features

### Mario Kart Track System
When implementing, consider:
- Track data model (metadata: name, cup, difficulty)
- Randomization algorithm (shuffle, weighted selection, constraints)
- Output format (JSON export, configuration file, seed-based reproduction)

### No External Dependencies Yet
Current approach: pure Python implementation. Add dependencies only when needed (e.g., `click` for CLI, `pydantic` for validation, `pytest` for testing).

## Common Tasks

### Expanding Beyond `main.py`
1. Create module structure in `src/`
2. Import modules in `main.py` 
3. Keep `main.py` thin — delegate logic to modules
4. Example: `from src.randomizer import RandomizerEngine` → `engine = RandomizerEngine(); engine.generate_track_list()`

### Adding CLI Arguments
Future: use `click` or `argparse` (not yet present). When added, update this guide.

### Testing Strategy
Future: Use `pytest` with tests in `tests/` directory (e.g., `tests/test_randomizer.py`). When implemented, follow Arrange-Act-Assert pattern.

## Notes for AI Agents
- This is a **greenfield project**; prioritize clear, simple implementations over premature optimization
- **No existing codebase patterns to preserve** — establish them as you grow the project
- Keep README.md updated as features are added
- When in doubt, prefer standard Python conventions (PEP 8, PEP 20)
