import bcrypt


def hash_password(plaintext: str) -> str:
    """
    Hashes a plaintext password using bcrypt.
    (https://pypi.org/project/bcrypt/)

    Parameters
    ----------
    plaintext: str
        The plaintext password to hash.

    Returns
    -------
    str
        The hashed password.

    """
    return bcrypt.hashpw(plaintext.encode(), bcrypt.gensalt(rounds=12)).decode()
