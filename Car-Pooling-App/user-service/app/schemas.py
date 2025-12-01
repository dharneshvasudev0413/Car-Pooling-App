from pydantic import BaseModel, EmailStr


# Base schema for shared fields
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr


# Schema for Registration
class UserCreate(UserBase):
    password: str


# Schema for Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for sending back user information
class UserResponse(UserBase):
    id: str

    class Config:
        from_attributes = True
