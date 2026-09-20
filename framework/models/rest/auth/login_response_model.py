from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field

JWT = Annotated[str, Field(min_length=1, pattern=r"^[\w-]+\.[\w-]+\.[\w-]+$")]


class LoginResponseModel(BaseModel):
    access_token: JWT
    refresh_token: JWT
    token_type: Literal["Bearer", "bearer"]
