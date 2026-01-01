# 🏎️ Mario Kart World Track Randomizer

A simple but powerful CLI tool for randomizing Mario Kart World track selection during tournaments. Get the randomized track selection that Mario Kart World doesn't natively provide!

## Overview

Mario Kart World lacks native track randomization features, making it difficult to run fair tournaments with unpredictable track rotations. This tool solves that problem by providing:

- **Seamless track randomization** — Shuffle through all 30 official tracks
- **Tournament-safe selection** — No track repeats within a tournament
- **Resume capability** — Exit and resume tournaments without losing progress
- **Simple JSON-based configuration** — Easy to understand and modify track lists

Perfect for tournament organizers, streamers, and casual players who want to add variety to their Mario Kart World sessions.

## Features

✨ **Core Features:**
- 🎲 Randomize track selection across all 30 official Mario Kart World tracks
- 🔄 **Resume tournaments** — Close the app mid-tournament and pick up where you left off
- 🚫 **No duplicate tracks** — Guaranteed each track appears only once per tournament
- 📊 **Progress tracking** — See how many tracks you've used and how many remain
- 🎮 **Simple user flow** — Press Enter for each track (perfect for streamers and tournaments)
- 📋 **Track management** — View all available tracks organized by cup

🔧 **Developer Features:**
- Built with **Typer** for a polished CLI experience
- **Emoji-driven output** for clarity and personality
- **JSON-based storage** for easy inspection and editing
- Python 3.13+ with modern type hints
- Managed by `uv` for fast, reliable dependency handling

## Installation

### Prerequisites
- Python 3.13 or higher
- `uv` package manager (or pip)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ALEKSI34/MarioKartWorldTrackRandomizer.git
   cd MarioKartWorldTrackRandomizer
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Run the application:**
   ```bash
   uv run python main.py --help
   ```

## Usage

### View Available Tracks

```bash
uv run python main.py tracks list
```

Output:
```
📋 Available Tracks (30 total)

  Mushroom Cup
     1. Mario Bros. Circuit (150cc)
     2. Moo Moo Meadows (150cc)
     3. Koopa Troopa Beach (150cc)
     4. Peach Beach (150cc)
  ...
```

### Start a Tournament

```bash
uv run python main.py tournament start
```

This will:
- Load all 30 tracks and shuffle them randomly
- Prompt you to press Enter for each track
- Display the next track and remaining count
- Save progress to `tournament_state.json`

Example flow:
```
🎮 Tournament started with 30 tracks!
📊 Tracks remaining: 30

Press Enter to get the next track... (Ctrl+C to exit)

🏁 Next Track: Bowser's Castle (Special Cup - 150cc)
📊 Tracks remaining: 29

🏁 Next Track: Rainbow Road (Special Cup - 150cc)
📊 Tracks remaining: 28
```

### Resume a Tournament

Simply run the same command again:
```bash
uv run python main.py tournament start
```

If you have an unfinished tournament, it will automatically resume from where you left off.

### Start a Fresh Tournament

To discard the current tournament and start anew:
```bash
uv run python main.py tournament start --new
```

### Check Tournament Progress

```bash
uv run python main.py tournament status
```

Output:
```
📊 Tournament Progress
   Used: 12/30 tracks
   Remaining: 18 tracks
   Status: 🏃 In progress (40%)
```

### Reset Current Tournament

```bash
uv run python main.py tournament reset --yes
```

(You'll be prompted for confirmation unless you add `--yes`)

### Initialize Example Tracks

```bash
uv run python main.py tracks init
```

This creates a fresh `tracks.json` file with all 30 official Mario Kart World tracks.

## Configuration

All tracks are stored in `tracks.json`. You can:
- **Edit tracks directly** — Open `tracks.json` and modify track names, cups, or difficulties
- **Remove tracks** — Delete entries to exclude certain tracks from randomization
- **Add custom tracks** — Add new entries following the same format

Example `tracks.json` entry:
```json
{
  "name": "Bowser's Castle",
  "cup": "Special Cup",
  "difficulty": "150cc"
}
```

## Project Structure

```
.
├── main.py                     # Typer CLI application
├── tracks.json                 # Track list (edit this!)
├── tournament_state.json       # Auto-generated tournament state
├── src/
│   ├── models/
│   │   └── track.py           # Track data model
│   ├── storage/
│   │   └── __init__.py        # File I/O operations
│   └── randomizer/
│       └── __init__.py        # Tournament session logic
└── .github/
    └── copilot-instructions.md # AI agent documentation
```

## How It Works

1. **Load Tracks** — Reads all tracks from `tracks.json`
2. **Shuffle** — Randomizes the track order once at tournament start
3. **Deliver** — Pops tracks from the shuffled list as you press Enter
4. **Persist** — Saves tournament state to `tournament_state.json`
5. **Resume** — On next run, loads existing state and continues

The key guarantee: **No track will appear twice in a single tournament** thanks to the pop-and-track pattern.

## Use Cases

- 📺 **Streaming tournaments** — Seamless track selection on stream
- 🎮 **Tournament organization** — Fair, unpredictable track rotations
- 👥 **Casual multiplayer** — Add variety to your Mario Kart World sessions
- 🎯 **Track practice** — Randomize which track you practice next

## Troubleshooting

**"tracks.json not found"**
```bash
uv run python main.py tracks init
```

**"No tournament in progress"**
Start one with:
```bash
uv run python main.py tournament start
```

**"All tracks have been used"**
Start a new tournament with:
```bash
uv run python main.py tournament start --new
```

## License

MIT License — Feel free to use, modify, and distribute!

## Disclaimer

⚠️ **AI-Generated Code Notice**

This project has been **largely generated using LLM models** (Large Language Models) including GitHub Copilot, Claude, and similar AI coding assistants. While the code has been reviewed and tested, please note:

- The implementation may not be optimal for all use cases
- Edge cases may not be fully covered
- Security implications of using AI-generated code should be considered
- Contributions and improvements are welcome

If you find bugs or have suggestions, please open an issue or submit a pull request!

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Improve documentation
- Submit pull requests

## Support

For issues or questions, please open a GitHub issue or contact the maintainers.

---

**Enjoy randomized Mario Kart World tournaments! 🏁**
