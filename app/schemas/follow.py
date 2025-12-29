from datetime import datetime
from pydantic import BaseModel, ConfigDict


class FollowCreate(BaseModel):
    followed_id: str


class FollowRead(BaseModel):
    follower_id: str
    followed_id: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class UserStats(BaseModel):
    user_id: str
    connections: int
    fans: int
