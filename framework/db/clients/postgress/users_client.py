from uuid import UUID

from settings import settings

from framework.db.clients.postgress.base_client import BasePostgresClient
from framework.db.models.postgres.users_db import UserRecordModel


class UsersDbClient(BasePostgresClient):
    """
    Postgres bd client for the `users` database.
    """

    def __init__(self):
        super().__init__(settings.user_db_url)

    def insert_user(self, user_row: UserRecordModel) -> None:
        """
        Inserts a user into the `users` table in the `users` database.

        Parameters
        ----------
        user_row: UserRecordModel
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

    def delete_user_by_email(self, email: str) -> None:
        """
        Deletes a user from the database based on their email.

        This method removes the user record associated with the provided email from
        the `users` table in the database. The operation is executed within a database
        connection and transaction context to ensure data consistency.

        Parameters
        ----------
        email : str
            The email address of the user to be removed from the database.

        Returns
        -------
        None
        """
        with self._pool.connection() as con, con.cursor() as cur:
            cur.execute("DELETE FROM users WHERE email = %(email)s", {"email": email})
            con.commit()
