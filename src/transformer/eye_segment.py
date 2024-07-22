from dataclasses import dataclass
from typing import List

@dataclass
class EyeSegment:
    x: int
    y: int
    width: int
    height: int

    def center(self):
        return (self.x + self.width // 2, self.y + self.height // 2)

    def size(self):
        return max(self.width, self.height)
