#retype
from pydantic import BaseModel, EmailStr
from typing import Optional


# Base schema for shared fields
class UserBase(BaseModel):
    firstName: str
    lastName: str
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

# JWT access token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Internal token data (after decoding JWT)
class TokenData(BaseModel):
    id: Optional[str] = None
    email: Optional[EmailStr] = None