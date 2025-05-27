from dataclasses import dataclass, field
from typing import List


@dataclass
class Star:
    name: str
    x: int
    y: int
    z: int
    size: float
    planets = []


@dataclass
class StarSystem:
    name: str
    galactic_x: int
    galactic_y: int
    galactic_z: int
    size: int
    security: float
    stars: List[Star] = field(default_factory=list)

    def add_star(self, name, x, y, z, size):
        self.stars.append(Star(name, x, y, z, size))