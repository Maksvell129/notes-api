from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse


class BaseHTTPException(Exception):
    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail


class NotFoundException(BaseHTTPException):
    pass


async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.detail},
    )
