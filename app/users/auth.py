from jose import jwt
from datetime import datetime, timedelta, timezone


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
        key="knklejrnkjckh",    # Секретный ключ для подписи токена
        algorithm="HS256"       # Алгоритм шифрования (HMAC с SHA-256)
    )
    return encoded_jwt  # возвращаем токен
