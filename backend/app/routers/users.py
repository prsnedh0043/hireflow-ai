from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import get_current_user_id
from app.models.user import User

router = APIRouter()


@router.get("/me")
def get_my_profile(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at
    }