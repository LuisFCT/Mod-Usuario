from db.usuario_db import UsuarioInDB
from db.usuario_db import buscar_user, crear_user, guardar_registro
from models.usuario_models import mostrar_user, registro_In, registro_Out

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()   #Creación de la api

#Operación Mostrar o listar usuario (GET)
@api.get("/listar/usuario/{CC_user}")
async def get_usuario(CC_user : int):
    usuario_in_db = buscar_user(CC_user)
    if usuario_in_db == None:
        raise HTTPException(status_code = 404, detail="El usuario no existe")
    usuario_out = mostrar_user(**usuario_in_db.dict())
    return usuario_out

#Operacion Crear usuario (POST)
@api.post("/crear/usuario/")
async def create_usuario(new_user : registro_In):
    new_user_in_db = buscar_user(new_user.CC_user)
    if new_user_in_db == None:
        new_user_in_db = UsuarioInDB(**new_user.dict() , Id_user = 3)
        new_user_in_db = guardar_registro(new_user_in_db)
        new_user_out = registro_Out(**new_user_in_db.dict())
        crear_user(new_user_out)
        return new_user_out
    return "No se puede registrar porque el Usuario ya existe"