from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

from pydantic import EmailStr

from app.config import settings
from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    assert isinstance(password, str), "Пароль должен быть строкой"
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Функция создаёт JWT-токен на основе переданных данных.
    :param data: словарь с данными пользователя (payload)
    :return: строка — закодированный JWT-токен
    #JWT Header.Payload.Signature
    """
    to_encode = data.copy()  # копируем входные данные, чтобы не изменять оригинальные данные
    expire = datetime.now(timezone.utc) + timedelta(days=30)  # срок действия 30 дней
    to_encode.update({"exp": expire})   # Добавляем в payload ключ 'exp' — обязательное поле для срока действия токена,
                                        # Без этого поля токен будет вечным
    encoded_jwt = jwt.encode(  # кодируем токен с помощью секрета и алгоритма HS256
        claims=to_encode,       # Данные, которые будут зашифрованы в токене
        key=settings.SECRET_KEY,    # Секретный ключ для подписи токена
        algorithm=settings.ENCODE_ALGORYTHM       # Алгоритм шифрования (HMAC с SHA-256)
    )
    return encoded_jwt  # возвращаем токен


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
