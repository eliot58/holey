from pydantic import BaseModel
from typing import Optional

class BunnyCreate(BaseModel):
    id: int
    invite_id: Optional[int]

class BunnyUpdate(BaseModel):
    id: int
    coins: int
    productivity: int
    experience: int
    endurance: int

class ClaimSchema(BaseModel):
    amount: int
    address: str