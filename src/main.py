from typing import TypeVar

from charclass import CharClass
from race import Race

BREAK = "-----"

RACES = [
    Race(
        name="Dragonborn",
        description="Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension. Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids. Some dragonborn are faithful servants to true dragons, others form the ranks of soldiers in great wars, and still others find themselves adrift, with no clear calling in life.",
        size="medium",
        speed=30,
        traits=[
            "Breath Weapon",
            "Damage Resistance to type associated with ancestry",
            "Languages - Common and Draconic",
        ],
    )
]
CHAR_CLASSES = [
    CharClass(
        name="Warlock",
        description="Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse. Through pacts made with mysterious beings of supernatural power, warlocks unlock magical effects both subtle and spectacular.",
        proficiencies=[
            "Armor - Light armor",
            "Weapons - Simple weapons",
            "Tools - None",
            "Saving throws - Wisdom, Charisma",
            "Skills - 2 from [Arcana, Deception, History, Intimidation, Investigation, Nature and Religion]",
        ],
        features=[
            "Hit dice - 1d8 per level",
            "HP @ Level 1 - 8 + Con. modifier",
            "HP @ higher levels - 1d8 (or 5) + Con. modifier per level after 1st",
        ],
        equipment=[
            "A light crossbow or any simple weapon",
            "a component pouch or arcane focus",
            "a scholer's oack or a dungeoneers pack",
            "Leather armor",
            "Any simple weapon",
            "Two daggers",
        ],
    )
]

T = TypeVar("T")


def select_option(options: list[T], prompt: str | None = None) -> T:
    # List options and return index of choice
    if prompt:
        print(prompt)

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    # TODO: Implement input
    print("\nEnter number choice:")
    index = 0
    choice = options[index]
    print(f"You have chosen: {choice}")
    return choice


def select_race():
    choice = select_option(RACES, "Select a race")


def select_class():
    choice = select_option(CHAR_CLASSES, "Choose a class")


STEPS = [select_race, select_class]


def main():
    print("Welcome player!\nIt's time to generate a new DND character")
    print(BREAK)
    for step in STEPS:
        step()
        print(BREAK)
    print("3. Determine your ability scores")
    print("4. Describe the character")
    print("5. Choose equipment")
    print("6. Party up!")


if __name__ == "__main__":
    main()
