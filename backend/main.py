from fastapi import FastAPI

from app.routers import health, auth, users

app = FastAPI()


app.include_router(health.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users")


@app.get("/")
def home():
    return {
        "message": "Welcome to HireFlow AI"
    }