from sqlalchemy import Column, Integer, String, JSON, Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)
    disabled = Column(Boolean)
    age = Column(Integer)
    preferences = Column(JSON)
    dislikes = Column(JSON)
    allergies = Column(JSON)
    last_meals = Column(JSON)
