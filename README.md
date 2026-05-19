# FastAPI Jenkins Demo

Proyecto de práctica para aprender integración continua y despliegue automático usando:

- FastAPI
- Docker
- Jenkins
- GitHub

---

# Tecnologías

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- Jenkins

---

# Estructura del proyecto

```text
.
├── app
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# Instalación

## 1. Clonar repositorio

```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_PROYECTO>
```

---

## 2. Crear entorno virtual

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar proyecto localmente

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

# Acceder a la aplicación

Aplicación:

```text
http://localhost:8000
```

Documentación Swagger:

```text
http://localhost:8000/docs
```

Redoc:

```text
http://localhost:8000/redoc
```

---

# Docker

## Construir imagen

```bash
docker build -t fastapi-demo .
```

---

## Ejecutar contenedor

```bash
docker run -d -p 8000:8000 --name fastapi-container fastapi-demo
```

---

# Jenkins

Este proyecto puede ser usado para practicar:

- CI/CD
- Pipelines
- Docker builds automáticos
- Deploy automático
- Integración con GitHub

---

# Pipeline básico Jenkins

```groovy
pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'URL_REPO'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f fastapi-container || true

                docker run -d \
                  --name fastapi-container \
                  -p 8000:8000 \
                  fastapi-demo
                '''
            }
        }
    }
}
```

---

# Objetivo de aprendizaje

Comprender el flujo moderno de desarrollo:

```text
Developer
    ↓
Git Push
    ↓
Jenkins Pipeline
    ↓
Docker Build
    ↓
Deploy
```