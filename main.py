from fastapi import FastAPI, Depends, HTTPException
from src.app.auth import AuthHandler
from src.app.config import settings
from src.models.schemas import AuthDetails
from src.routes.api import api_router

settings.PROJECT_NAME = "SigoAPI"

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}"
)

app.include_router(api_router, prefix=settings.API_V1_STR)