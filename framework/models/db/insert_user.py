from framework.models.db.user_row import UserRow


class InsertUser(UserRow):
    """
    A `UserRow` seeded directly into the database for tests, paired with its plaintext password.

    The `users` table only stores the hashed password, so the plaintext value has to be carried
    alongside the row - it's necessary to log the user in through the UI/API but can't be recovered
    from `hashed_password` afterward.
    """

    password: str
