from src.domain.entities.lane import Lane
from src.domain.entities.vehicle import Vehicle
from src.domain.entities.traffic_light import TrafficLight


def test_lane_starts_empty():
    lane = Lane(lane_id="lane-1", direction="north", traffic_light=TrafficLight(light_id="tl-1"))
    assert lane.is_empty()
    assert lane.queue_length() == 0


def test_enqueue_vehicle_increases_queue_length():
    lane = Lane(lane_id="lane-1", direction="north", traffic_light=TrafficLight(light_id="tl-1"))
    lane.enqueue_vehicle(Vehicle(vehicle_id="car-1", arrival_time=0.0))
    assert lane.queue_length() == 1
    assert not lane.is_empty()


def test_dequeue_vehicle_returns_front_of_queue_fifo():
    lane = Lane(lane_id="lane-1", direction="north", traffic_light=TrafficLight(light_id="tl-1"))
    lane.enqueue_vehicle(Vehicle(vehicle_id="car-1", arrival_time=0.0))
    lane.enqueue_vehicle(Vehicle(vehicle_id="car-2", arrival_time=1.0))

    dequeued = lane.dequeue_vehicle()
    assert dequeued.vehicle_id == "car-1"
    assert lane.queue_length() == 1


def test_dequeue_from_empty_lane_returns_none():
    lane = Lane(lane_id="lane-1", direction="north", traffic_light=TrafficLight(light_id="tl-1"))
    assert lane.dequeue_vehicle() is None

def test_can_vehicles_proceed_only_when_green():
    light = TrafficLight(light_id="tl-1")
    lane = Lane(lane_id="lane-1", direction="north", traffic_light=light)

    assert not lane.can_vehicles_procceed()  

    light.switch_phase() 
    assert lane.can_vehicles_procceed()