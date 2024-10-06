from src.charclass import CharClass
from src.race import Race

BREAK = "-----"

ABILITIES = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
]
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
