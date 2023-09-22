import os
from sqlalchemy import create_engine # me sirve para crear el motor de base de datos
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # me sirve para manipular las tablas de la base 

sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}' # con esto creaomos la URL de la base de datos

engine = create_engine(database_url, echo=True) # este seria el motor de la base de datos

Session = sessionmaker(bind=engine) # esrta es la secion para conectarme a la base de datos o enlazarme con la base

Base = declarative_base()