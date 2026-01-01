"""Mario Kart World Track Randomizer CLI application."""
import sys

import typer

from src.models.track import Track
from src.randomizer import TournamentSession
from src.storage import get_tracks_file, load_tracks, save_tracks

app = typer.Typer(help="🏎️ Mario Kart World Track Randomizer for tournaments")
tournament_app = typer.Typer(help="Tournament management")
tracks_app = typer.Typer(help="Track management")

app.add_typer(tournament_app, name="tournament")
app.add_typer(tracks_app, name="tracks")


@tournament_app.command(name="start")
def tournament_start(new: bool = typer.Option(False, "--new", "-n", help="Start a fresh tournament (reset existing)")) -> None:
    """Start or resume a tournament."""
    try:
        session = TournamentSession()

        if new or not session.used_tracks:
            session.start_new()
            used, total = session.get_progress()
            typer.echo("")
            typer.echo(f"🎮 Tournament started with {total} tracks!")
            typer.echo(f"📊 Tracks remaining: {session.get_remaining_count()}")
        else:
            used, total = session.get_progress()
            typer.echo("")
            typer.echo(f"📝 Resuming tournament...")
            typer.echo(f"📊 Progress: {used}/{total} tracks used")
            typer.echo(f"📊 Tracks remaining: {session.get_remaining_count()}")

        typer.echo("")
        typer.echo("Press Enter to get the next track... (Ctrl+C to exit)")
        typer.echo("")

        while not session.is_complete():
            input()  # Wait for user to press Enter
            track = session.get_next_track()
            if track:
                typer.echo(f"🏁 Next Track: {track}")
                typer.echo(f"📊 Tracks remaining: {session.get_remaining_count()}")
                typer.echo("")

        typer.echo("🎉 Tournament complete! All tracks have been used.")
        typer.echo("Start a new tournament with: mkwr tournament start --new")

    except FileNotFoundError as e:
        typer.echo(str(e), err=True)
        typer.echo(f"💡 Create {get_tracks_file()} with your tracks:", err=True)
        typer.echo("   mkwr tracks list  # (after adding example tracks)", err=True)
        raise typer.Exit(1)
    except ValueError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)


@tournament_app.command(name="status")
def tournament_status() -> None:
    """Show tournament progress."""
    try:
        session = TournamentSession()
        used, total = session.get_progress()

        if used == 0:
            typer.echo("❌ No tournament in progress.")
            return

        typer.echo(f"📊 Tournament Progress")
        typer.echo(f"   Used: {used}/{total} tracks")
        typer.echo(f"   Remaining: {session.get_remaining_count()} tracks")
        if session.is_complete():
            typer.echo("   Status: ✅ Complete")
        else:
            percent = (used / total) * 100
            typer.echo(f"   Status: 🏃 In progress ({percent:.0f}%)")

    except FileNotFoundError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)


@tournament_app.command(name="reset")
def tournament_reset(confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation")) -> None:
    """Reset the current tournament."""
    try:
        if not confirm:
            if not typer.confirm("⚠️  Are you sure you want to reset the tournament?"):
                typer.echo("❌ Reset cancelled.")
                return

        session = TournamentSession()
        session.reset()
        typer.echo("✅ Tournament reset. Start a new one with: mkwr tournament start")

    except FileNotFoundError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)


@tracks_app.command(name="list")
def tracks_list() -> None:
    """List all available tracks."""
    try:
        tracks = load_tracks()
        typer.echo("")
        typer.echo(f"📋 Available Tracks ({len(tracks)} total)")
        typer.echo("")

        current_cup = None
        for i, track in enumerate(tracks, 1):
            if track.cup != current_cup:
                current_cup = track.cup
                typer.echo(f"  {current_cup}")

            typer.echo(f"    {i:2d}. {track.name} ({track.difficulty})")

        typer.echo("")

    except FileNotFoundError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)
    except ValueError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)


@tracks_app.command(name="init")
def tracks_init() -> None:
    """Initialize tracks.json with example tracks."""
    tracks_file = get_tracks_file()

    if tracks_file.exists():
        if not typer.confirm(f"⚠️  {tracks_file} already exists. Overwrite?"):
            typer.echo("❌ Operation cancelled.")
            return

    example_tracks = [
        Track("Luigi Circuit", "Mushroom Cup", "150cc"),
        Track("Moo Moo Meadows", "Mushroom Cup", "150cc"),
        Track("Coconut Mallory", "Mushroom Cup", "150cc"),
        Track("Mario Circuit", "Mushroom Cup", "150cc"),
        Track("Daisy Cruiser", "Flower Cup", "150cc"),
        Track("Dry Dry Desert", "Flower Cup", "150cc"),
        Track("Mushroom Bridge", "Flower Cup", "150cc"),
        Track("Mario Circuit 2", "Flower Cup", "150cc"),
    ]

    save_tracks(example_tracks)
    typer.echo(f"✅ {tracks_file} initialized with {len(example_tracks)} example tracks.")
    typer.echo("💡 Edit the file to customize your tracks, or use other tracks.")


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
