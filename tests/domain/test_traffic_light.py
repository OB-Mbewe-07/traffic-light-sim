import pytest
from src.domain.entities.traffic_light import TrafficLight, LightPhase

def test_traffic_light_starts_red_by_default():
    light = TrafficLight(light_id="intersection-1-north")
    assert light.phase == LightPhase.RED
    assert light.is_red()    

def test_switch_phase_follows_legal_cycle():
    light = TrafficLight(light_id="intersection-1-north")

    light.switch_phase()
    assert light.phase == LightPhase.GREEN

    light.switch_phase()
    assert light.phase == LightPhase.YELLOW

    light.switch_phase()
    assert light.phase == LightPhase.RED

def test_switch_phase_resets_time_in_phase():
    light = TrafficLight(light_id="intersection-1-north")
    light.tick(10.0)
    assert light.time_in_phase == 10.0

    light.switch_phase()
    assert light.time_in_phase == 0.0

def test_tick_accumulates_time():
    light = TrafficLight(light_id="intersection-1-north")
    light.tick(5.0)
    light.tick(2.5)
    assert light.time_in_phase == 7.5


def test_tick_rejects_negative_delta():
    light = TrafficLight(light_id="intersection-1-north")
    with pytest.raises(ValueError):
        light.tick(-1.0)