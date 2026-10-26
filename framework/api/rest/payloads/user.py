from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RegisterPayload:
    email: str
    password: str
    full_name: str

    def __str__(self) -> str:
        return f"email={self.email!r}, full_name={self.full_name!r}, password={self.password}"


@dataclass(frozen=True, slots=True)
class LoginPayload:
    username: str
    password: str

    def __str__(self) -> str:
        return f"username={self.username!r}, password={self.password!r}"
