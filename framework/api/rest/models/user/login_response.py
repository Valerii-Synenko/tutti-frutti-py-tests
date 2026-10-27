from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

JWT = Annotated[str, Field(pattern=r"^[\w-]+\.[\w-]+\.[\w-]+$")]


# Login
class LoginUserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    access_token: JWT
    refresh_token: JWT
    token_type: Literal["Bearer", "bearer"]
