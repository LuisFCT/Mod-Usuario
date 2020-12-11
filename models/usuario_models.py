from pydantic import BaseModel

class mostrar_user(BaseModel):
    Id_user : int
    nombre_user : str
    apellido_user : str
    CC_user : int
    email : str
    telefono : str


class registro_In(BaseModel):
    nombre_user : str
    apellido_user : str
    CC_user : int
    email : str
    telefono : str

class registro_Out(BaseModel):
    Id_user : int
    nombre_user : str
    apellido_user : str
    CC_user : int
    email : str
    telefono : str
