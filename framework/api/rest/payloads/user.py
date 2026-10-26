from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RegisterPayload:
    email: str | None = None
    password: str | None = None
    full_name: str | None = None

    def __str__(self) -> str:
        return f"email={self.email!r}, password={self.password!r}, full_name={self.full_name!r}"


@dataclass(frozen=True, slots=True)
class LoginPayload:
    username: str
    password: str

    def __str__(self) -> str:
        return f"username={self.username!r}, password={self.password!r}"
