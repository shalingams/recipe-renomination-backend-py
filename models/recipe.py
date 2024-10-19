from sqlalchemy import Column, Integer, String, JSON, Boolean
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    ingredients = Column(JSON)
    allergens = Column(JSON)
    preferences = Column(JSON)
    seasonality = Column(JSON)
    metadata = Column(JSON)
    last_suggested = Column(JSON)
