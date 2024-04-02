from fastapi import HTTPException
from fastapi import status


class BaseHTTPException(HTTPException):
    status_code = None

    def __init__(self, **kwargs) -> None:
        super().__init__(status_code=self.status_code, **kwargs)


class NotFoundException(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
