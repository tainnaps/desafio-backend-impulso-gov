from dataclasses import dataclass
from typing import TypedDict

from fastapi import HTTPException

from src.model import EstablishmentModel


class Establishment(TypedDict):
    cnes: str
    nome: str
    latitude: float
    longitude: float


@dataclass
class EstablishmentController:
    __model: EstablishmentModel = EstablishmentModel()

    def get_all_by_city_id(self, city_id: int) -> list[Establishment]:
        establishments = self.__model.get_all_by_city_id(city_id=city_id)

        return [
            {
                "cnes": id_cnes,
                "nome": name,
                "latitude": latitude,
                "longitude": longitude,
            }
            for id_cnes, name, latitude, longitude in establishments
        ]

    def get_by_cnes_id(self, cnes_id: int) -> Establishment:
        establishment = self.__model.get_by_cnes_id(cnes_id=cnes_id)

        if not establishment:
            raise HTTPException(
                status_code=404, detail="Establishment not found"
            )

        id_cnes, name, latitude, longitude = establishment

        return {
            "cnes": id_cnes,
            "nome": name,
            "latitude": latitude,
            "longitude": longitude,
        }
