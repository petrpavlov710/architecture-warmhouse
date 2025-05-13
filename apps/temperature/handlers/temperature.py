from fastapi import APIRouter, Query

from schemas.temperature import TemperatureLocation
from utils.location_sensor_matcher import (
    get_location_by_sensor_id,
    get_sensor_id_by_location,
)

temperature_router = APIRouter()


@temperature_router.get("/temperature/", response_model=TemperatureLocation)
async def get_temperature_by_location(location: str = Query()):
    sensor_id = get_sensor_id_by_location(location)

    return TemperatureLocation(
        location=location,
        sensor_id=sensor_id,
        description=f"Temperature in location {location}",
    )


@temperature_router.get("/temperature/{sensor_id}", response_model=TemperatureLocation)
async def get_temperature_by_sensor_id(sensor_id: str):
    location = get_location_by_sensor_id(sensor_id)
    return TemperatureLocation(
        location=location,
        sensor_id=sensor_id,
        description=f"Temperature for sensor {sensor_id}",
    )
