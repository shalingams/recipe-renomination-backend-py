from typing import List
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    full_name: str
    email: str | None = None
    password: str | None = None
    disabled: bool | None = None
    age: int
    preferences: List[str]
    dislikes: List[str]
    allergies: List[str]
    last_meals = {"date": date, "meals": List[str]}


class Recipe(BaseModel):
    title: str
    ingredients: List
    allergens: List
    preferences: List  # like vegetarian, pesco-vegetarian
    seasonality: List  # e.g., "winter", "summer"
    metadata = {
        "nutritional_info": List[str],
        "cuisine": List[str],
        "popularity": List[str],  # could be weighted by popularity
        "meal_type": List[str],  # "breakfast", "lunch", "dinner"
    }
    last_suggested: date
