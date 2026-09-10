from src.domain.entities.lane import Lane
from src.domain.entities.vehicle import Vehicle


def test_lane_starts_empty():
    lane = Lane(lane_id="lane-1", direction="north")
    assert lane.is_empty()
    assert lane.queue_length() == 0


def test_enqueue_vehicle_increases_queue_length():
    lane = Lane(lane_id="lane-1", direction="north")
    lane.enqueue_vehicle(Vehicle(vehicle_id="car-1", arrival_time=0.0))
    assert lane.queue_length() == 1
    assert not lane.is_empty()


def test_dequeue_vehicle_returns_front_of_queue_fifo():
    lane = Lane(lane_id="lane-1", direction="north")
    lane.enqueue_vehicle(Vehicle(vehicle_id="car-1", arrival_time=0.0))
    lane.enqueue_vehicle(Vehicle(vehicle_id="car-2", arrival_time=1.0))

    dequeued = lane.dequeue_vehicle()
    assert dequeued.vehicle_id == "car-1"
    assert lane.queue_length() == 1


def test_dequeue_from_empty_lane_returns_none():
    lane = Lane(lane_id="lane-1", direction="north")
    assert lane.dequeue_vehicle() is None