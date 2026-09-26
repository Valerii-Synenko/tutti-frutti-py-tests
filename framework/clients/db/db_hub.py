from functools import cached_property

from framework.clients.db.postgress.users_client import UsersDbClient


class DbHub:
    """
    Aggregates connections to databases.
    """

    @cached_property
    def users_db(self) -> UsersDbClient:
        return UsersDbClient()

    def close_all(self) -> None:
        """
        Closes all connections these that were opened.
        """
        for name in ("users_db", "orders_db"):
            if name in self.__dict__:
                getattr(self, name).close_connection()
