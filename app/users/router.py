from fastapi import APIRouter
from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.schemas import SUser_register
from app.exceptions import UserAlreadyExistsException

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)


@router.post("/register", summary="Регистрация нового пользователя")
async def register_user(user_data: SUser_register):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException(user_data.email)

    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)

    return {"message": "Пользователь успешно зарегистрирован."}
