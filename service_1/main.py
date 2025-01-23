from fastapi import FastAPI, HTTPException
import jwt
import datetime

app = FastAPI()
SECRET_KEY = "007secret"

@app.post("/generate-token/")
def generate_token():
    payload = {
        "mission": "Agent 007, you accomplished the mission!",
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return {"token": token}