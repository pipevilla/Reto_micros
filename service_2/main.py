from fastapi import FastAPI, HTTPException, Header
import jwt

app = FastAPI()
SECRET_KEY = "007secret"

@app.post("/validate-token/")
def validate_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token missing")

    token = authorization.split(" ")[1]  # <token>
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"status": "valid", "user": decoded["user"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired: >5min")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")