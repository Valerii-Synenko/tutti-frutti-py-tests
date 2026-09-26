from collections.abc import Callable, Generator
from uuid import UUID

import pytest
from faker import Faker
from framework.db.db_hub import DbHub
from framework.db.models.db.insert_user import InsertUser
from framework.utils.hashing import hash_password
from playwright.sync_api import APIRequestContext, Playwright


@pytest.fixture
def api_context(playwright: Playwright) -> Generator[APIRequestContext]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def db_aggregator():
    aggregator = DbHub()
    yield aggregator
    aggregator.close_all()


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def insert_user_into_db(faker, db_aggregator):
    created_ids: list[UUID] = []

    def _insert_user(*, is_admin: bool = False, is_seller: bool = False) -> InsertUser:
        password = faker.password(length=8)
        hashed_password = hash_password(password)
        user = InsertUser(
            id=faker.uuid4(cast_to=None),
            email=faker.email(),
            hashed_password=hashed_password,
            full_name=faker.name(),
            created_at=faker.date_time(),
            is_admin=is_admin,
            is_seller=is_seller,
            password=password,
        )

        db_aggregator.users_db.insert_user(user)
        created_ids.append(user.id)
        return user

    yield _insert_user

    for user_id in created_ids:
        db_aggregator.users_db.delete_user_by_id(user_id)


@pytest.fixture
def admin_user(insert_user_into_db: Callable[..., InsertUser]) -> InsertUser:
    return insert_user_into_db(is_admin=True)
