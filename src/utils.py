from typing import TypeVar

T = TypeVar("T")


def select_option(prompt: str, options: list[T]) -> T:
    # List options and return index of choice
    print(prompt)

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    index = int_input("Enter number choice:")
    choice = options[index]
    print(f"You have chosen: {choice}")
    return choice


def str_input(prompt: str) -> str:
    # TODO: Implement
    print(prompt)
    return "Test Str"


def int_input(prompt: str) -> int:
    # TODO: Implement
    print(prompt)
    return 0
