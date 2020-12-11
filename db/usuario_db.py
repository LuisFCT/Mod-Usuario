from typing import Dict
from pydantic import BaseModel

class UsuarioInDB(BaseModel):
    Id_user : int
    nombre_user : str
    apellido_user : str
    CC_user : int
    email : str
    telefono : str

#Base de datos ficticia
DB_usuarios = Dict[int, UsuarioInDB]

#Usuarios iniciales en la base de datos
DB_usuarios = {
    1085990345 : UsuarioInDB(**{"Id_user" : 1,
                                "nombre_user" : "Nairo", 
                                "apellido_user":"Quintana",
                                "CC_user" : 1085990345,
                                "email":"Nairo@gmail.com",
                                "telefono": 3127778}),

    87564876 : UsuarioInDB(**{ "Id_user" : 2,
                                "nombre_user" : "Carlos", 
                                "apellido_user":"Vives",
                                "CC_user" : 87564876,
                                "email":"Cvives@gmail.com",
                                "telefono": 7775665}),

    37976489 : UsuarioInDB(**{  "Id_user" : 3,
                                "nombre_user" : "Natalia", 
                                "apellido_user":"Paris",
                                "CC_user" : 37976489,
                                "email":"nataliaparis@gmail.com",
                                "telefono": 2259867})
}

#Funciones sobre la base de datos
def buscar_user(CC : int):
    if CC in DB_usuarios.keys():
        return DB_usuarios[CC]
    else:
        return None

def crear_user(usuario : UsuarioInDB):
    DB_usuarios[usuario.CC_user]= usuario    
    return DB_usuarios

registros = []  #Se define una lista vacia para el registro
generator = {"id_us":3}

def guardar_registro(registro_in_db : UsuarioInDB):
    generator["id_us"] = generator["id_us"] + 1
    registro_in_db.Id_user = generator["id_us"]
    registros.append(registro_in_db)
    return registro_in_db

