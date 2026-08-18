from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to HireFlow AI"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "HireFlow AI backend"
    }


@app.get("/api/about")
def about():
    return {
        "name": "HireFlow AI",
        "version": "0.1.0",
        "description": "AI-powered recruitment and career intelligence platform"
    }