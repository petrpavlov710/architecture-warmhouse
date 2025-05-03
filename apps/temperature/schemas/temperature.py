import datetime
import random

from pydantic import BaseModel, Field


class TemperatureLocation(BaseModel):
    sensor_id: str
    location: str
    value: float = Field(
        default_factory=lambda: round(random.uniform(-20, 80), 1),
    )
    description: str
    unit: str = "Celsius"
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(),
    )
    status: str = 'Active'
    sensor_type: str = "Temperature"
