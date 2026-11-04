from framework.api.rest.payloads.user import RegisterPayload

NEGATIVE_REGISTRATION_CASES = (
    (
        RegisterPayload(email="jane.tester@example.com", password="Password1!"),  # noqa: S106
        ["body", "full_name"],
        "Input should be a valid string",
    ),
    (
        RegisterPayload(password="Password1!", full_name="Jane Tester"),  # noqa: S106
        ["body", "email"],
        "Input should be a valid string",
    ),
    (
        RegisterPayload(email="jane.tester@example.com", full_name="Jane Tester"),
        ["body", "password"],
        "Input should be a valid string",
    ),
)
