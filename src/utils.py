from typing import TypeVar

import click

T = TypeVar("T")


def select_option(prompt: str, options: list[T]) -> T:
    # List options and return index of choice
    click.echo(prompt)

    for i, option in enumerate(options):
        click.echo(f"{i + 1}. {option}")

    index = int_input("Enter number choice") - 1
    choice = options[index]
    click.echo(f"You have chosen: {choice}")
    return choice


def str_input(prompt: str) -> str:
    return click.prompt(prompt)


def int_input(prompt: str) -> int:
    return click.prompt(prompt, type=int)
