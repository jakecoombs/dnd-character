from dataclasses import dataclass


@dataclass
class CharClass:
    name: str
    description: str
    features: list[str]
    proficiencies: list[str]
    equipment: list[str]

    def __str__(self) -> str:
        return self.name

    def summary(self) -> str:
        return f"{self.name} - {self.description}"
