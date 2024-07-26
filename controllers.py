import models
from fastapi import Response

def get_users():
    return {"users": list(models.users_model)} 

def create_new_user(user: models.User ):
    # for usr in models.users_model:
    #     if usr.email == user.email:
    #         response.status_code = 400
    #         return {"status": "error", "message": "Email já cadastrado."} 
    models.users_model.append(user)
    return {"status": "success", "message": "Usuário criado com sucesso!"}

def user_login(email: str, password: str, response: Response):
    for usr in models.users_model:
        if usr.email == email and usr.password == password:
            response.status_code = 200
            return {"status": "success", "message": "Usuário logado com sucesso!"}
        
    response.status_code = 404
    return {"status": "error", "message": "Usuário não encontrado."}
