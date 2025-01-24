from fastapi import FastAPI, HTTPException
import jwt
import datetime
import requests

app = FastAPI()
SECRET_KEY = "007secret"

# Función para generar un token JWT
@app.post("/generate-token/")
def generate_token():    
    # Definimos la carga útil del token con un mensaje y una expiración de 5 minutos    
    payload = {
        "Mission": "Valid token Agent 007, you accomplished the mission!",
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=5)
    }
    # Codificamos el token usando la clave secreta y el algoritmo HS256
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    if token:
        # Si el token se generó correctamente, nos comunicamos con el servicio 2
        result = communicate_with_service_2(token)
        return {
            "Response": result.get("Mission"),
            "Token": token  # Aquí incluimos el valor del token en la respuesta
        }

# Función para comunicarse con el servicio 2 y validar el token
def communicate_with_service_2(token):
    url = "http://service-2.default.svc.cluster.local:8001/validate-token"
    headers = {"Authorization": f"Token: {token}"}
    # Realizamos una solicitud POST al servicio 2 con el token en los encabezados
    response = requests.post(url, headers=headers)
    # Retornamos la respuesta del servicio 2
    return response.json()