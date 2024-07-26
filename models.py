from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    is_employee: bool  

users_model: list[User] = [
    User(name="Vinicius", email="vg@bionutri.com", password="junior", is_employee=True)  
]
