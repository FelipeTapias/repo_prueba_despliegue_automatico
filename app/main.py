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
        "mensaje": f"Hola {nombre}, espero estes bien..."
    }

@app.get("/loteria/{numero}")
def saludo(numero: str):
        if("123" == numero):
            return { "mensaje:": "Eres el feliz ganador..."}
        else:
             return { "mensaje:": "Eres el triste perdedor..."}
    
