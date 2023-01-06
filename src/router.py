from fastapi import APIRouter

from src.controller import EstablishmentController

controller = EstablishmentController()
router = APIRouter()
