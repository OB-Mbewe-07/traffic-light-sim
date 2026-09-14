from src.domain.entities.intersection import Intersection
from src.domain.entities.lane import Lane
from src.domain.entities.vehicle import Vehicle


def test_intersection_starts_with_no_lanes():
    intersection = Intersection(intersection_id="main-1st")
    assert intersection.total_queue_length() == 0
    assert intersection.get_lane("north") is None


def test_add_lane_and_retrieve_by_direction():
    intersection = Intersection(intersection_id="main-1st")
    north_lane = Lane(lane_id="lane-n", direction="north")
    intersection.add_lane(north_lane)

    retrieved = intersection.get_lane("north")
    assert retrieved is north_lane


def test_total_queue_length_sums_across_lanes():
    intersection = Intersection(intersection_id="main-1st")

    north_lane = Lane(lane_id="lane-n", direction="north")
    north_lane.enqueue_vehicle(Vehicle(vehicle_id="car-1", arrival_time=0.0))
    north_lane.enqueue_vehicle(Vehicle(vehicle_id="car-2", arrival_time=1.0))

    south_lane = Lane(lane_id="lane-s", direction="south")
    south_lane.enqueue_vehicle(Vehicle(vehicle_id="car-3", arrival_time=2.0))

    intersection.add_lane(north_lane)
    intersection.add_lane(south_lane)

    assert intersection.total_queue_length() == 3


def test_queue_lengths_by_direction():
    intersection = Intersection(intersection_id="main-1st")

    north_lane = Lane(lane_id="lane-n", direction="north")
    north_lane.enqueue_vehicle(Vehicle(vehicle_id="car-1", arrival_time=0.0))

    east_lane = Lane(lane_id="lane-e", direction="east")

    intersection.add_lane(north_lane)
    intersection.add_lane(east_lane)

    result = intersection.queue_lengths_by_direction()
    assert result == {"north": 1, "east": 0}