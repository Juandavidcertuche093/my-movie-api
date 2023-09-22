from config.database import Base 
from sqlalchemy import Column, Integer, String, Float

# vamos a crear las tablas de la base de datos (peliculas)
class Movie(Base):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key= True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)