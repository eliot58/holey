from fastapi import APIRouter, Depends
from .models import Bunny, Bunny_Schema
from .schemas import *

router = APIRouter(
    tags=["bunny"]
)

@router.get("/bunny/{id}", response_model = Bunny_Schema)
async def get_bunny(id: int):
    bunny = await Bunny.filter(tg_id = id).first()
    return bunny

@router.post("/bunny")
async def create_bunny(data: BunnyCreate):
    return {"status": "success", "detail": None, "data": None}


@router.patch("/bunny")
async def update_bunny(data: BunnyUpdate):
    return {"status": "success", "detail": None, "data": None}


@router.post("/claim")
async def claim(data: ClaimSchema):
    return {"status": "success", "detail": None, "data": None}
