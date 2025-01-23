from fastapi import FastAPI, HTTPException, Header
import jwt

app = FastAPI()
SECRET_KEY = "007secret"

@app.post("/validate-token/")
def validate_token(Authorization: str = Header(None)):
    if not Authorization:
        raise HTTPException(status_code=401, detail="Token missing")

    token = Authorization.split(" ")[1]  # <token>
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"Mission": "Valid token, you can pass!", "Mission": decoded["Mission"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired, >5min... Try again agent!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token, you shall not pass!")