"""Storage operations for tracks."""
import json
from pathlib import Path
from typing import Any

from src.models.track import Track


def get_tracks_file() -> Path:
    """Get the path to tracks.json file."""
    return Path("tracks.json")


def load_tracks() -> list[Track]:
    """Load tracks from tracks.json.

    Returns:
        List of Track objects.

    Raises:
        FileNotFoundError: If tracks.json doesn't exist.
        ValueError: If tracks.json is empty or invalid.
    """
    tracks_file = get_tracks_file()

    if not tracks_file.exists():
        raise FileNotFoundError(
            f"❌ {tracks_file} not found. Please create it with your track list."
        )

    with open(tracks_file) as f:
        data = json.load(f)

    if not data or not isinstance(data, list):
        raise ValueError(
            f"❌ {tracks_file} is empty or invalid. Please add tracks to it."
        )

    tracks = [
        Track(name=item["name"], cup=item["cup"], difficulty=item["difficulty"])
        for item in data
    ]

    if not tracks:
        raise ValueError(f"❌ No tracks found in {tracks_file}")

    return tracks


def save_tracks(tracks: list[Track]) -> None:
    """Save tracks to tracks.json.

    Args:
        tracks: List of Track objects to save.
    """
    tracks_file = get_tracks_file()
    data = [
        {"name": track.name, "cup": track.cup, "difficulty": track.difficulty}
        for track in tracks
    ]
    with open(tracks_file, "w") as f:
        json.dump(data, f, indent=2)


def load_tournament_state() -> dict[str, Any] | None:
    """Load the current tournament state if it exists.

    Returns:
        Tournament state dict or None if file doesn't exist.
    """
    state_file = Path("tournament_state.json")
    if not state_file.exists():
        return None

    with open(state_file) as f:
        return json.load(f)


def save_tournament_state(state: dict[str, Any]) -> None:
    """Save the current tournament state.

    Args:
        state: Tournament state dictionary.
    """
    state_file = Path("tournament_state.json")
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def clear_tournament_state() -> None:
    """Clear the tournament state file."""
    state_file = Path("tournament_state.json")
    if state_file.exists():
        state_file.unlink()
