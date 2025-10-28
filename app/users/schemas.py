from pydantic import BaseModel, EmailStr


class SUser_register(BaseModel):
    email: EmailStr
    password: str