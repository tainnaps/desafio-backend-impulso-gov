from fastapi import APIRouter

from src.controller import EstablishmentController

controller = EstablishmentController()
router = APIRouter()


router.add_api_route(
    "/listarEstabelecimentosPorMunicipio/{city_id}",
    endpoint=controller.get_all_by_city_id,
    methods=["GET"],
)
