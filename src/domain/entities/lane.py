from dataclasses import dataclass, field
from enum import Enum
from src.domain.entities.vehicle import Vehicle

class LaneDirection(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

@dataclass
class Lane:
    lane_id: str
    direction: LaneDirection
    vehicles: list[Vehicle] = field(default_factory=list)

    def enqueue_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicles.append(vehicle)

    def dequeue_vehicle(self) -> Vehicle | None:
        if not self.vehicles:          
            return None
        return self.vehicles.pop(0)

    def queue_length(self) -> int:
        return len(self.vehicles)

    def is_empty(self) -> bool:
        return len(self.vehicles) == 0
        