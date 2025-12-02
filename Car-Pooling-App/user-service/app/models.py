from sqlalchemy import Column, String
from app.db import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable = False)
    hashed_password = Column(String(255), nullable = False)
