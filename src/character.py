import click

from src.ability import Ability
from src.charclass import CharClass
from src.consts import ABILITIES, BREAK, CHAR_CLASSES, RACES
from src.race import Race
from src.utils import int_input, select_option, str_input


class Character:
    name: str
    race: Race
    charclass: CharClass
    abilities: list[Ability]

    def __init__(self) -> None:
        click.echo("Welcome player!\nIt's time to generate a new DND character")
        click.echo(BREAK)
        self.race = select_option(prompt="Select a race", options=RACES)
        click.echo(BREAK)
        self.charclass = select_option(prompt="Choose a class", options=CHAR_CLASSES)
        click.echo(BREAK)
        self.assign_ability_scores(self.roll_for_abilities())
        click.echo(BREAK)
        self.name = str_input(f"Name your {self.race} {self.charclass}")
        click.echo(BREAK)
        click.echo("Choose equipment")

    def ability_roll(self) -> int:
        click.echo("Roll 4d6")
        rolls = [int_input(f"Roll {j+1}") for j in range(0, 4)]
        rolls.remove(min(rolls))
        total = sum(rolls)
        click.echo(f"The total of the highest 3 dice: {total}")
        return total

    def roll_for_abilities(self) -> list[int]:
        click.echo("Roll for your 6 ability scores")
        return [self.ability_roll() for _ in range(0, 6)]

    def assign_ability_scores(self, ability_scores: list[int]) -> None:
        click.echo("Assign each of your rolled scores to an ability")
        abilities = []
        for ability_name in ABILITIES:
            ability = Ability(ability_name)
            score = int_input(f"Select a score for {ability} from {ability_scores}")
            ability.set_score(score)
            ability_scores.remove(score)
        self.abilities = abilities

    def __str__(self) -> str:
        return f"{self.name} the {self.race} {self.charclass}"
