from sqlalchemy.orm import Session
from sqlalchemy import and_, exists
from fastapi import HTTPException, status
from app.models.follow import Follow
from app.models.user import User


def follow_user(db: Session, follower_id: str, followed_id: str) -> Follow:
    if follower_id == followed_id:
        raise HTTPException(status_code=400, detail="Cannot follow yourself")
    
    if not db.get(User, follower_id):
        raise HTTPException(status_code=404, detail="Follower not found")
    if not db.get(User, followed_id):
        raise HTTPException(status_code=404, detail="User to follow not found")
    
    existing = db.query(Follow).filter(
        and_(Follow.follower_id == follower_id, Follow.followed_id == followed_id)
    ).first()
    if existing:
        raise HTTPException(status_code=409, detail="Already following this user")
    
    follow = Follow(follower_id=follower_id, followed_id=followed_id)
    db.add(follow)
    db.commit()
    db.refresh(follow)
    return follow


def unfollow_user(db: Session, follower_id: str, followed_id: str) -> None:
    follow = db.query(Follow).filter(
        and_(Follow.follower_id == follower_id, Follow.followed_id == followed_id)
    ).first()
    if not follow:
        raise HTTPException(status_code=404, detail="Not following this user")
    db.delete(follow)
    db.commit()


def get_connections_count(db: Session, user_id: str) -> int:
    subquery = db.query(Follow.follower_id).filter(
        and_(Follow.followed_id == user_id)
    ).subquery()
    
    count = db.query(Follow).filter(
        and_(
            Follow.follower_id == user_id,
            Follow.followed_id.in_(subquery)
        )
    ).count()
    return count


def get_fans_count(db: Session, user_id: str) -> int:
    followers = db.query(Follow).filter(Follow.followed_id == user_id).all()
    
    fans = 0
    for f in followers:
        mutual = db.query(Follow).filter(
            and_(Follow.follower_id == user_id, Follow.followed_id == f.follower_id)
        ).first()
        if not mutual:
            fans += 1
    return fans


def get_user_stats(db: Session, user_id: str) -> dict:
    if not db.get(User, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user_id,
        "connections": get_connections_count(db, user_id),
        "fans": get_fans_count(db, user_id)
    }
