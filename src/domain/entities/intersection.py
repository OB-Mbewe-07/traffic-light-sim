from dataclasses import dataclass
from src.domain.entities.lane import Lane

@dataclass
class Intersection:
    Intersection_id: str
    lanes: list[Lane] = field(default_factory=list)

    def add_lane(self, lane: Lane) -> None:
        self.lanes.append(lane)

    def get_lane(self, direction: str) -> None | Lane:
        for lane in self.lanes:
            if lane.direction == direction:
                return lane
        return None

    def total_queue_length(self) -> int:
        return sum(lane.queue_length for lane in self.lanes)

    def queue_lengths_by_direction(self) -> dict[str, int]:
        return {lane.direction: lane.queue_length for lane in self.lanes}


