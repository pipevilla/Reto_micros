from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import datetime

app = FastAPI()
SECRET_KEY = "007secret"

SERVICE_2_URL = "http://localhost:8001/validate-token"

class User(BaseModel):
    username: str
    password: str

@app.post("/generate-token/")
def generate_token(user: User):
    payload = {
        "mission": "Agent 007, you accomplished the mission!",
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(SERVICE_2_URL, headers=headers)
    
    if response.status_code == 200:
        return {"message": "Token validado correctamente con el servicio 2", "details": response.json()}
    else:
        return {"message": "Error al validar el token con el servicio 2", "details": response.json()}
    
    
    #return {"token": token}