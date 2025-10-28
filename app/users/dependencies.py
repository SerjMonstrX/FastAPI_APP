from http.client import HTTPException

from fastapi import Request


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=401, details="Не найден токен")
    return token

def get_current_user(token):

    return "user"