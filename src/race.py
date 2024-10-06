from dataclasses import dataclass


@dataclass
class Race:
    name: str
    description: str
    size: str
    speed: int
    traits: list[str]

    def __str__(self) -> str:
        return self.name

    def summary(self) -> str:
        return f"{self.name} - {self.description}"
