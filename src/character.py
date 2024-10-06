from src.charclass import CharClass
from src.consts import BREAK, CHAR_CLASSES, RACES
from src.race import Race
from src.utils import select_option, str_input


class Character:
    name: str
    race: Race
    charclass: CharClass

    def __init__(self) -> None:
        print("Welcome player!\nIt's time to generate a new DND character")
        print(BREAK)
        self.race = select_option(prompt="Select a race", options=RACES)
        print(BREAK)
        self.charclass = select_option(prompt="Choose a class", options=CHAR_CLASSES)
        print(BREAK)
        print("3. Determine your ability scores")
        self.name = str_input(f"Name your {self.race} {self.charclass}:")
        print("5. Choose equipment")

    def __str__(self) -> str:
        return self.name
