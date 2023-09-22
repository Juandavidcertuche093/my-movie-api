from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

#nueva ruta listado de peliculas o consultado de las peliculas
@movie_router.get('/movies', tags=['movies'], response_model=list[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) # 
def get_movies() -> list[Movie]:
    db = Session()
    result = MovieService(db).get_movies()    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


#nueva ruta pero con un parametro {id} esto nos sirve para filtrar las peliculas por su ID
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db). get_movie(id) # filter este metodo me sirve para filtrar la informacion de las peliculas 
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content= jsonable_encoder(result)) 

# este nos sirve para filtrar por categoria
@movie_router.get('/movies/', tags=['movies'], response_model=list[Movie]) #
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> list[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))
    
#metodo POST en este caso lo vamos a utilizar para registrar una pelicula 
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha resgistrado la pelicula'})

# metodo PUT actualizar 
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})

# metodo DELETE para eliminar peliculas 
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
