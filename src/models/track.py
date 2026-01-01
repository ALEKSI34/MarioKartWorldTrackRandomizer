"""Track data model."""
from dataclasses import dataclass


@dataclass
class Track:
    """Represents a Mario Kart World track."""

    name: str
    cup: str
    difficulty: str = "150cc"

    def __str__(self) -> str:
        """Return formatted track information."""
        return f"{self.name} ({self.cup} - {self.difficulty})"

    def __hash__(self) -> int:
        """Return hash based on track name (for uniqueness)."""
        return hash(self.name)
