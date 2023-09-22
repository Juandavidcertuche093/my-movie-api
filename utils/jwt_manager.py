from jwt import encode, decode

# creamos la funcion para crear el token
def create_token(data: dict):
    token: str = encode(payload=data, key='my_secrete_key', algorithm='HS256')
    return token

#creamos la funcion para validar el token
def validate_token(token: str) -> dict:
    data: dict = decode(token, key='my_secrete_key', algorithms=['HS256'])
    return data



