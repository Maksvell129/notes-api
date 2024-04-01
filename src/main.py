import uvicorn
from fastapi import FastAPI

from src.api.routers import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
