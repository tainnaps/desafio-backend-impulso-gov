from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from src.router import router

app = FastAPI()


app.include_router(router)


@app.get("/")
def initialize_app():
    return {"message": "Webservice OK"}


@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return JSONResponse({"message": exc.detail}, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc: RequestValidationError):
    message = str(exc).replace("\n", " ").replace("   ", " ")
    return JSONResponse({"message": message}, status_code=400)
