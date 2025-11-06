import sys
import click
from sdsrc.normalize import normalize_whitespace
from sdsrc.textutils import count_words, reverse_words


def read_text(text: str | None) -> str:
    """
    If text is provided as an argument, use it.
    Otherwise read from standard input (stdin).
    """
    if text is not None:
        return text

    # read piped input: cat file | sd normalize
    data = sys.stdin.read().strip()
    return data


@click.group()
def cli() -> None:
    """Command-line tools for text processing."""
    pass


@cli.command()
@click.argument("text", required=False)
def normalize(text: str | None) -> None:
    """Normalize whitespace in TEXT."""
    click.echo(normalize_whitespace(read_text(text)))


@cli.command()
@click.argument("text", required=False)
def count(text: str | None) -> None:
    """Count words in TEXT."""
    click.echo(count_words(read_text(text)))


@cli.command()
@click.argument("text", required=False)
def reverse(text: str | None) -> None:
    """Reverse words in TEXT."""
    click.echo(reverse_words(read_text(text)))
