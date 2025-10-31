from datetime import datetime, timezone

from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError

from app.config import settings
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=401, details="Не найден токен")
    return token

async def get_current_user(token: str = Depends):
    try:
        payload = jwt.decode(
            token=token, key=settings.SECRET_KEY, algorithms=settings.ENCODE_ALGORYTHM
        )

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if not expire or (int(expire)< datetime.now(timezone.utc).timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id:str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user
