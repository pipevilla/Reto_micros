import requests

def communicate_with_service_2(token):
    url = "http://localhost:8001/validate-token/"
    headers = {"Authorization": f"Token: {token}"}
    response = requests.post(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    token_response = requests.post("http://localhost:8000/generate-token/").json()
    token = token_response.get("token")
    if token:
        result = communicate_with_service_2(token)
        print(result)