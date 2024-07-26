from fastapi import APIRouter, Response
import controllers
import dtos

router = APIRouter()

@router.get("/users")
def get_users():
    return controllers.get_users()

@router.post("/login")
def user_login(credentials: dtos.UserLogin, response: Response):
    return controllers.user_login(
        email = credentials.email, 
        password = credentials.password,
        response=response
    )

@router.post("/users")
def create_new_user(user: dtos.RegisterUser):
    return controllers.create_new_user(user)

