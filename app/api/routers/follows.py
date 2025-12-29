from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, verify_auth
from app.schemas.follow import FollowRead, UserStats
from app.crud import follows as crud

router = APIRouter(prefix="/users", tags=["follows"], dependencies=[Depends(verify_auth)])


@router.post("/{user_id}/follow/{target_id}", response_model=FollowRead, status_code=status.HTTP_201_CREATED)
def follow_user(user_id: str, target_id: str, db: Session = Depends(get_db)) -> FollowRead:
    return crud.follow_user(db, user_id, target_id)


@router.delete("/{user_id}/follow/{target_id}", status_code=status.HTTP_204_NO_CONTENT)
def unfollow_user(user_id: str, target_id: str, db: Session = Depends(get_db)) -> None:
    crud.unfollow_user(db, user_id, target_id)
    return None


@router.get("/{user_id}/stats", response_model=UserStats)
def get_user_stats(user_id: str, db: Session = Depends(get_db)) -> UserStats:
    return crud.get_user_stats(db, user_id)
