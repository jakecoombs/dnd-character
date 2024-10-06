import click

from src.character import Character


def main():
    character = Character()
    click.echo(f"Safe travels {character}!")


if __name__ == "__main__":
    main()
