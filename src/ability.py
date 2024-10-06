from math import floor

import click


class Ability:
    name: str
    score: int
    modifier: int

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def set_score(self, score: int) -> None:
        self.score = score
        self.modifier = floor((score - 10) / 2)
        click.echo(f"For a score of {self.score}, the modifer is {self.modifier}")
