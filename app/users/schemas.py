from pydantic import BaseModel, EmailStr, ConfigDict

class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    # На будущее, если понадобится совместимость с ORM
    model_config = ConfigDict(from_attributes=True)