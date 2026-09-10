from enum import Enum
from dataclasses import dataclass

class LightPhase(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

_NEXT_PHASE = {
    LightPhase.RED: LightPhase.GREEN,
    LightPhase.YELLOW: LightPhase.RED,
    LightPhase.GREEN: LightPhase.YELLOW
}

@dataclass
class TrafficLight:
    light_id : str
    phase : LightPhase = LightPhase.RED
    time_in_phase : float = 0

    def tick(self, seconds : float) -> None:
        if seconds < 0:
            raise ValueError("Seconds must be non-negative")
        self.time_in_phase += seconds

    def switch_phase(self) -> None:
        self.phase = _NEXT_PHASE[self.phase]
        self.time_in_phase = 0.0

    def is_green(self) -> bool:
        return self.phase == LightPhase.GREEN

    def is_red(self) -> bool:
        return self.phase == LightPhase.RED

    def is_yellow(self) -> bool:
        return self.phase == LightPhase.YELLOW