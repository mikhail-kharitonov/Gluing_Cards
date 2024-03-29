from src.models.zone_type_model import ZoneType
from typing import List, Optional

from pydantic import BaseModel, Field
class Zone(BaseModel):
    zone_type: ZoneType = Field(alias="zoneType")
    zone_length: List[int] = Field(alias="zoneLength")
    zone_hydrograph: List[int] = Field(alias="zoneHydrograph")



