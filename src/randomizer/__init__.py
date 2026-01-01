"""Tournament session management."""
import random
from datetime import datetime

from src.models.track import Track
from src.storage import (
    clear_tournament_state,
    load_tournament_state,
    load_tracks,
    save_tournament_state,
)


class TournamentSession:
    """Manages a tournament session for randomizing Mario Kart tracks."""

    def __init__(self) -> None:
        """Initialize or resume a tournament session."""
        self.all_tracks = load_tracks()
        self.used_tracks: list[str] = []
        self.remaining_tracks: list[Track] = []
        self._load_or_init()

    def _load_or_init(self) -> None:
        """Load existing tournament or initialize a new one."""
        state = load_tournament_state()

        if state:
            # Resume existing tournament
            self.used_tracks = state.get("used_tracks", [])
            # Reconstruct remaining tracks by filtering used ones
            used_names = set(self.used_tracks)
            self.remaining_tracks = [
                track for track in self.all_tracks if track.name not in used_names
            ]
        else:
            # Start fresh tournament
            self.remaining_tracks = self.all_tracks.copy()
            random.shuffle(self.remaining_tracks)
            self.used_tracks = []

    def start_new(self) -> None:
        """Start a fresh tournament, clearing any existing one."""
        clear_tournament_state()
        self.used_tracks = []
        self.remaining_tracks = self.all_tracks.copy()
        random.shuffle(self.remaining_tracks)
        self._save_state()

    def get_next_track(self) -> Track | None:
        """Get the next track in the tournament.

        Returns:
            The next Track, or None if all tracks have been used.
        """
        if not self.remaining_tracks:
            return None

        track = self.remaining_tracks.pop(0)
        self.used_tracks.append(track.name)
        self._save_state()
        return track

    def is_complete(self) -> bool:
        """Check if all tracks have been used.

        Returns:
            True if no tracks remain, False otherwise.
        """
        return len(self.remaining_tracks) == 0

    def get_progress(self) -> tuple[int, int]:
        """Get tournament progress.

        Returns:
            Tuple of (used_count, total_count).
        """
        return len(self.used_tracks), len(self.all_tracks)

    def get_remaining_count(self) -> int:
        """Get number of remaining tracks.

        Returns:
            Count of tracks not yet used.
        """
        return len(self.remaining_tracks)

    def reset(self) -> None:
        """Reset the current tournament."""
        clear_tournament_state()
        self.used_tracks = []
        self.remaining_tracks = self.all_tracks.copy()
        random.shuffle(self.remaining_tracks)

    def _save_state(self) -> None:
        """Save current tournament state to file."""
        state = {
            "timestamp": datetime.now().isoformat(),
            "used_tracks": self.used_tracks,
            "total_tracks": len(self.all_tracks),
        }
        save_tournament_state(state)
