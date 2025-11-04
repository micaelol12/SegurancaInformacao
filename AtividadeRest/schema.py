
from pydantic import BaseModel,EmailStr,ConfigDict

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    senha: str

class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class UserList(BaseModel):
    users: list[UserPublic]
