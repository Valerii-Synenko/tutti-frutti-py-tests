from uuid import UUID

from settings import settings

from framework.clients.db.postgress.base_client import BasePostgresClient
from framework.models.db.user_row import UserRow


class UsersDbClient(BasePostgresClient):
    """
    Postgres bd client for the `users` database.
    """

    def __init__(self):
        super().__init__(settings.user_db_url)

    def insert_user(self, user_row: UserRow) -> None:
        """
        Inserts a user into the `users` table in the `users` database.

        Parameters
        ----------
        user_row: UserRow
            The user row model to insert.
        """
        with self._pool.connection() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO users "
                "(id, email, hashed_password, full_name, created_at, is_admin, is_seller) "
                "VALUES "
                "(%(id)s, %(email)s, %(hashed_password)s, %(full_name)s, "
                "%(created_at)s, %(is_admin)s, %(is_seller)s)",
                user_row.model_dump(),
            )
            con.commit()

    def delete_user_by_id(self, user_id: UUID) -> None:
        """
        Deletes a user from the `users` table in the `users` db.

        Parameters
        ----------
        user_id: UUID
            The id of the user to delete.
        """
        with self._pool.connection() as con, con.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %(id)s", {"id": user_id})
            con.commit()
