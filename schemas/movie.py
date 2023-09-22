from pydantic import BaseModel, Field
from typing import Optional 


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5,max_length=50) # esto es para tener el valor por defecto y el tamaño minimo y maximo de caracteres
    overview: str = Field(min_length=5,max_length=100)
    year: int = Field(le=2023) # cuando son valores enteros
    rating: float = Field(default=10, ge=1, le=10)
    category: str = Field(default='categoria', min_length=1, max_length=20)

    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                'title': 'Mi pelicula',
                'overview': 'Descripcion de la pelicula',
                'year': 2022,
                'rating': 9.8,
                'category': 'Acción'
            }
        }

