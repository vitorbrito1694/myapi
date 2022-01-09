import uvicorn
from fastapi import APIRouter

from src.routes.endpoints import login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)