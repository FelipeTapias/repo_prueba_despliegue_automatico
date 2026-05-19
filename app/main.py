from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hola desde FastAPI"
    }


@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {
        "mensaje": f"Hola {nombre}"
    }