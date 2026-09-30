from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserRecordModel(BaseModel):
    id: UUID
    email: str
    hashed_password: str
    full_name: str
    created_at: datetime
    is_admin: bool
    is_seller: bool
