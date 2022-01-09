import uvicorn
from fastapi import FastAPI
# from src.app.config import settings
from src.routes.api import api_router

# settings.PROJECT_NAME = "SigoAPI"
# settings.API_V1_STR = "/SigoAPI/v1"

app = FastAPI(title="SigoAPI")

app.include_router(api_router, prefix="/SigoAPI/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)