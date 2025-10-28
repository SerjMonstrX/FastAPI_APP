from fastapi import HTTPException, status


class UserAlreadyExistsException(HTTPException):
    def __init__(self, email: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Пользователь с email '{email}' уже существует.",
        )


class UserNotFoundException(HTTPException):
    def __init__(self, email: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Пользователь с email '{email}' не найден.",
        )


class IncorrectPasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный пароль.",
        )


class IncorrectPasswordOrUsernameException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль.",
        )

class BookingNotFoundException(HTTPException):
    def __init__(self, booking_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Бронирование с id={booking_id} не найдено.",
        )
