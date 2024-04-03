import uvicorn
from fastapi import FastAPI

from src.api.routers import router
from src.exceptions import not_found_exception_handler
from src.exceptions import NotFoundException

app = FastAPI()

app.include_router(router)

app.add_exception_handler(NotFoundException, not_found_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
