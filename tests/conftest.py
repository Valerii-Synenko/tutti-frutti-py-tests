import os
import warnings
from collections.abc import Callable, Generator
from datetime import datetime
from uuid import UUID

import pytest
from faker import Faker
from framework.api.api_hub import ApiHub
from framework.api.rest.models.user.user_request import RegisterUserRequestModel
from framework.db.db_hub import DbHub
from framework.utils.qase import fetch_case_titles
from framework.utils.user import AuthenticatedUser, create
from playwright.sync_api import APIRequestContext, Playwright
from qase.pytest import qase
from qase.pytest.plugin import QasePytestPlugin


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    """Sets a default Qase run title before the qase-pytest plugin reads its config."""
    os.environ.setdefault("QASE_TESTOPS_RUN_TITLE", f"Run from local {datetime.now():%Y-%m-%d %H:%M}")


def pytest_collection_modifyitems(config, items):
    """Titles results in Qase runs after their linked test cases instead of the test function names."""
    if (config.getoption("qase_mode", default=None) or os.environ.get("QASE_MODE")) != "testops":
        return

    linked_items = {
        item: ids[0]
        for item in items
        if not item.get_closest_marker("qase_title") and (ids := QasePytestPlugin.get_qase_ids(item))
    }
    if not linked_items:
        return

    try:
        titles = fetch_case_titles(set(linked_items.values()))
    except (OSError, KeyError, ValueError) as e:
        warnings.warn(f"Could not fetch test case titles from the Qase TestOps: {e}", stacklevel=1)
        return

    for item, case_id in linked_items.items():
        if title := titles.get(case_id):
            item.add_marker(qase.title(title))


@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> Generator[APIRequestContext]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def db_hub() -> Generator[DbHub]:
    aggregator = DbHub()
    yield aggregator
    aggregator.close_all()


@pytest.fixture(scope="session")
def api_hub(api_context) -> ApiHub:
    return ApiHub(api_context)


@pytest.fixture(scope="session")
def faker() -> Faker:
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
def buyer_user(create_user: Callable[..., AuthenticatedUser]) -> AuthenticatedUser:
    return create_user()


@pytest.fixture
def user_for_registration(faker, db_hub):
    user_payload = RegisterUserRequestModel(
        full_name=f"{faker.first_name()} {faker.last_name()}",
        email=faker.email(),
        password=faker.password(length=8),
    )

    yield user_payload

    db_hub.users_db.delete_user_by_email(user_payload.email)
