from fastapi import APIRouter

from src.api.endpoints import board
from src.api.endpoints import note

router = APIRouter(prefix="")

router.include_router(note.router, prefix="/notes", tags=["notes"])
router.include_router(board.router, prefix="/boards", tags=["boards"])
