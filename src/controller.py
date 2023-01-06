from dataclasses import dataclass
from typing import TypedDict

from src.model import EstablishmentModel


class Establishment(TypedDict):
    cnes: str
    nome: str
    latitude: float
    longitude: float


@dataclass
class EstablishmentController:
    __model: EstablishmentModel = EstablishmentModel()
