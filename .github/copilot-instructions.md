# AI Coding Agent Instructions - Mario Kart World Track Randomizer

## Project Overview
This is a Python project (3.13+) for randomizing Mario Kart World tracks in tournaments. Uses Typer for CLI, with track storage in JSON format. The project uses uv and pyproject.toml for dependency management.

## Key Architecture Patterns

### Project Structure
- **`main.py`**: Typer CLI application with tournament and tracks commands
- **`pyproject.toml`**: Dependency and metadata management (uv, typer 0.9.0+)
- **`tracks.json`**: User-maintained JSON file with track definitions (name, cup, difficulty)
- **`tournament_state.json`**: Auto-generated session state (created during tournament)
- **`src/models/track.py`**: Track dataclass (name, cup, difficulty)
- **`src/storage/__init__.py`**: File I/O for tracks.json and tournament_state.json
- **`src/randomizer/__init__.py`**: TournamentSession class with session management
- **`README.md`**: Project documentation

### Python Version & Environment
- Requires Python 3.13+
- Use `.python-version` file to specify the Python version
- uv handles virtual environment and dependencies via `pyproject.toml`

## Development Workflow

### Running the Project
```bash
uv run python main.py --help
uv run python main.py tournament start
uv run python main.py tracks list
```

Or install and run directly:
```bash
uv sync
mkwr tournament start
mkwr tracks list
```

### Adding Dependencies
- Use `uv add <package>` to add dependencies (updates `pyproject.toml` automatically)
- Update the `requires-python` constraint in `pyproject.toml` if needed
- uv generates `uv.lock` for reproducible builds

### Key Commands
- `mkwr tournament start [--new]` — Start/resume tournament (press Enter for each track)
- `mkwr tournament status` — Show progress (used/remaining tracks)
- `mkwr tournament reset [--yes]` — Clear tournament state
- `mkwr tracks list` — Display all available tracks
- `mkwr tracks init` — Initialize example tracks.json (overwrites existing)

## Code Organization Conventions

### Current Implementation
- **`main.py`** — Typer CLI with three command groups: `tournament` and `tracks`
- **`src/models/`** — Track dataclass with `__str__` and `__hash__` for set operations
- **`src/storage/`** — Functions: `load_tracks()`, `save_tracks()`, `load_tournament_state()`, `save_tournament_state()`, `clear_tournament_state()`, `get_tracks_file()`
- **`src/randomizer/`** — TournamentSession class handling shuffle, state persistence, and track selection

### Data Models
**Track** (dataclass):
- `name: str` — Track name
- `cup: str` — Cup name (e.g., "Mushroom Cup")
- `difficulty: str` — Difficulty level (e.g., "150cc")

**Tournament State** (JSON):
```json
{
  "timestamp": "2026-01-01T12:00:00",
  "used_tracks": ["Luigi Circuit", "Moo Moo Meadows"],
  "total_tracks": 48
}
```

**Tracks** (JSON):
```json
[
  {"name": "Luigi Circuit", "cup": "Mushroom Cup", "difficulty": "150cc"},
  ...
]
```

### Naming & Patterns
- Use snake_case for module and function names
- Use PascalCase for class names
- Emoji-driven UX: 🏁 track, 📊 progress, ✅ success, ❌ error, 💡 info, 🎮 start, 🎉 completion
- No track repetition within a tournament (enforced by pop-and-track pattern)

### Key Design Decisions
1. **Resume behavior**: TournamentSession auto-loads existing state from `tournament_state.json` on init
2. **Randomization**: Shuffle entire list once at tournament start, pop from front for FIFO delivery
3. **Uniqueness**: Track names used as unique identifiers (set-based tracking in `used_tracks`)
4. **Isolation**: storage module handles all file I/O; randomizer module handles logic only

## Integration Points & Features

### Tournament User Flow
1. User runs `mkwr tournament start`
2. TournamentSession loads `tracks.json` and existing tournament_state.json (if any)
3. If new tournament: shuffle tracks, save state
4. If resuming: restore used_tracks and remaining_tracks from state
5. Loop: user presses Enter → `get_next_track()` → pop from remaining → append to used → save state
6. When remaining empty: display completion message

### Tracks Management
- `tracks.json` is user-maintained; users edit directly or use `tracks init` to bootstrap
- No API for adding tracks via CLI (intentional simplicity)
- Example tracks provided in `tracks init` command

### Error Handling
- Missing `tracks.json` → FileNotFoundError with helpful guidance
- Empty `tracks.json` → ValueError with error message
- Tournament completion → Friendly message to start new tournament with `--new`

## Common Tasks

### Adding New Tournament Commands
1. Create function in `main.py` with `@tournament_app.command()` decorator
2. Access TournamentSession for state management
3. Use typer.echo() for output (supports emoji)
4. Follow error handling pattern: try-except with typer.Exit(1)

### Modifying Track Fields
1. Update `Track` dataclass in `src/models/track.py`
2. Update `tracks.json` structure
3. Update storage layer: `load_tracks()` and `save_tracks()` parsing logic
4. Update example in `tracks_init()` command

### Testing
Future: Use `pytest` with tests in `tests/` directory. Follow Arrange-Act-Assert pattern.
Key test areas: TournamentSession.get_next_track(), resume behavior, storage load/save.

### Extending Tournament Features
Future considerations: seeded randomization, weighted tracks, character bans, CSV export, web UI
Always preserve: resume behavior, JSON persistence, emoji UX, no-duplicate guarantee

## Notes for AI Agents
- **Core guarantee**: No track appears twice in a tournament (enforced by `used_tracks` set + pop logic)
- **Resume-first design**: Tournament state persists; `TournamentSession.__init__()` auto-resumes or starts fresh
- **File-driven**: All data stored as JSON (tracks.json, tournament_state.json); easy for users to inspect/edit
- **Typer CLI**: Rich help, emoji output, confirmation prompts for destructive ops
- Keep user-facing text concise and emoji-driven for clarity in terminal
- When in doubt, follow standard Python conventions (PEP 8, PEP 20)
