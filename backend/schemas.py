from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    name: str
    genres: str
    image_url: str