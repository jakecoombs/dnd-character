import click

from src.charclass import CharClass
from src.consts import BREAK, CHAR_CLASSES, RACES
from src.race import Race
from src.utils import select_option, str_input


class Character:
    name: str
    race: Race
    charclass: CharClass

    def __init__(self) -> None:
        click.echo("Welcome player!\nIt's time to generate a new DND character")
        click.echo(BREAK)
        self.race = select_option(prompt="Select a race", options=RACES)
        click.echo(BREAK)
        self.charclass = select_option(prompt="Choose a class", options=CHAR_CLASSES)
        click.echo(BREAK)
        click.echo("Determine your ability scores")
        click.echo(BREAK)
        self.name = str_input(f"Name your {self.race} {self.charclass}")
        click.echo(BREAK)
        click.echo("Choose equipment")

    def __str__(self) -> str:
        return f"{self.name} the {self.race} {self.charclass}"
