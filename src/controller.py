from dataclasses import dataclass

from src.model import EstablishmentModel


@dataclass
class EstablishmentController:
    __model: EstablishmentModel = EstablishmentModel()
