from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest

router = APIRouter()


@router.post("/register")
def register_user(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):
    # Check whether email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email is already registered"
        )

    # Hash password
    password_hash = hash_password(user.password)

    # Create user
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=password_hash
    )

    # Save user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }
@router.post("/login")
def login_user(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == credentials.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        credentials.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(user.id)

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }