from pydantic import BaseModel

# se crea una clase para el usuario y contraseña
class User(BaseModel):
    email:str
    password:str