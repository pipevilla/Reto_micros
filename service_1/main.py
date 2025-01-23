from fastapi import FastAPI, HTTPException
import jwt
import datetime
import requests

app = FastAPI()
SECRET_KEY = "007secret"

@app.post("/generate-token/")
def generate_token():
    payload = {
        "Mission": "Agent 007, you accomplished the mission!",
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    if token:
        result = communicate_with_service_2(token)
        return {"Response:": result.get("Mission")}


def communicate_with_service_2(token):
    url = "http://service_2:8001/validate-token"
    headers = {"Authorization": f"Token: {token}"}
    response = requests.post(url, headers=headers)
    return response.json()