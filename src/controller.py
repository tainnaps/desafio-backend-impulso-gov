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

