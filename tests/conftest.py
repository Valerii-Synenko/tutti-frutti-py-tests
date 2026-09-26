from collections.abc import Callable, Generator
from uuid import UUID

import pytest
from faker import Faker
from framework.api.api_hub import ApiHub
from framework.db.db_hub import DbHub
from framework.utils.user import AuthenticatedUser, create
from playwright.sync_api import APIRequestContext, Playwright


@pytest.fixture
def api_context(playwright: Playwright) -> Generator[APIRequestContext]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def db_hub():
    aggregator = DbHub()
    yield aggregator
    aggregator.close_all()


@pytest.fixture
def api_hub(api_context: APIRequestContext) -> ApiHub:
    return ApiHub(api_context)


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def create_user(faker, db_hub, api_hub):
    created_users_ids: list[UUID] = []

    def _create_user(*, is_admin: bool = False, is_seller: bool = False) -> AuthenticatedUser:
        user = create(faker, db_hub.users_db, api_hub.auth_client, is_admin=is_admin, is_seller=is_seller)
        created_users_ids.append(user.id)
        return user

    yield _create_user

    for user_id in created_users_ids:
        db_hub.users_db.delete_user_by_id(user_id)


@pytest.fixture
def admin_user(create_user: Callable[..., AuthenticatedUser]) -> AuthenticatedUser:
    return create_user(is_admin=True)
