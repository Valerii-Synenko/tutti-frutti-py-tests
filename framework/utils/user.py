from faker import Faker

from framework.api.clients.rest import AuthClient
from framework.api.models.rest.rest.user.login_response import LoginResponseModel
from framework.db.clients.postgress.users_client import UsersDbClient
from framework.db.models.db.user_row import UserRow
from framework.utils.hashing import hash_password


class InsertUserIntoDB(UserRow):
    """
    A `UserRow` seeded directly into the database for tests, paired with its plaintext password.

    The `users` table only stores the hashed password, so the plaintext value has to be carried
    alongside the row - it's necessary to log the user in through the UI/API but can't be recovered
    from `hashed_password` afterward.
    """

    password: str


class AuthenticatedUser(InsertUserIntoDB):
    """
    The authenticated user object.

    Attributes
    ----------
    bearer_token: str
        The bearer token used for authentication.
    """

    bearer_token: str


def create(
    faker: Faker,
    users_db: UsersDbClient,
    auth_client: AuthClient,
    *,
    is_admin: bool = False,
    is_seller: bool = False,
) -> AuthenticatedUser:
    """
    Creates a user in the `users` database and logs him through the API using the `AuthClient` client.

    Parameters
    ----------
    faker: Faker
        The Faker instance used to generate random data for the user such as email and password, etc.
    users_db: UsersDbClient
        The client used to insert a user into the `users` database.
    auth_client: AuthClient
        The client used to authenticate a user via API request.
    is_admin: bool
        Whether the user should be an admin.
    is_seller: bool
        Whether the user should be a seller.

    Returns
    -------
    AuthenticatedUser
        The authenticated user object.
    """
    email = faker.email()
    password = faker.password(length=8)
    hashed_password = hash_password(password)

    user_row = UserRow(
        id=faker.uuid4(cast_to=None),
        email=email,
        hashed_password=hashed_password,
        full_name=faker.name(),
        created_at=faker.date_time(),
        is_admin=is_admin,
        is_seller=is_seller,
    )
    users_db.insert_user(user_row)

    response = auth_client.user_login(email, password)
    bearer_token = LoginResponseModel.model_validate(response.json()).access_token

    return AuthenticatedUser(
        **user_row.model_dump(),
        password=password,
        bearer_token=bearer_token,
    )
