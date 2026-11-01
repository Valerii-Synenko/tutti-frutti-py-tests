from framework.api.rest.payloads.user import RegisterPayload

NEGATIVE_REGISTRATION_CASES = (
    (
        RegisterPayload("jane.tester@example.com", "Password1!", ""),
        ["body", "full_name"],
        "String should have at least 1 character",
    ),
    (
        RegisterPayload("", "Password1!", "Jane Tester"),
        ["body", "email"],
        "value is not a valid email address: An email address must have an @-sign.",
    ),
    (
        RegisterPayload("jane.tester@example.com", "", "Jane Tester"),
        ["body", "password"],
        "String should have at least 8 characters",
    ),
)
