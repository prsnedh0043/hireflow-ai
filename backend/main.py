from fastapi import FastAPI
from app.routers import health, auth

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to HireFlow AI"
    }


@app.get("/api/about")
def about():
    return {
        "name": "HireFlow AI",
        "version": "0.1.0",
        "description": "AI-powered recruitment and career intelligence platform"
    }


app.include_router(health.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth")