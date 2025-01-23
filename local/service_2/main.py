from fastapi import FastAPI, HTTPException, Header
import jwt

app = FastAPI()
SECRET_KEY = "007secret"

# Endpoint para validar el token JWT
@app.post("/validate-token/")
def validate_token(Authorization: str = Header(None)):
    # Verificamos si el encabezado de autorización está bien formado
    if not Authorization:
        raise HTTPException(status_code=401, detail="Token missing")
    
    # Extraemos el token del encabezado de autorización
    token = Authorization.split(" ")[1]  # <token>
    try:
        # Decodificamos el token usando la clave secreta y el algoritmo HS256
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"Mission": "Valid token, you can pass!", "Mission": decoded["Mission"]}
    except jwt.ExpiredSignatureError:
        # Manejo de excepción si el token ha expirado, >5min
        raise HTTPException(status_code=401, detail="Token expired, >5min... Try again agent!")
    except jwt.InvalidTokenError:
        # Excepción si el token es inválido o malformado
        raise HTTPException(status_code=401, detail="Invalid token, you shall not pass!")