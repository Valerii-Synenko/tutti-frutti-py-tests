from uuid import UUID

import psycopg
from psycopg.rows import dict_row
from settings import settings

from framework.models.db.user_row import UserRow


class UsersDb:
    def __init__(self):
        self.users_db_host = settings.user_db_url

    def insert_user(self, user_row: UserRow) -> None:
        """
        Inserts a user into the database.

        Parameters
        ----------
        user_row: UserRow
            The user row model to insert.
        """
        with (
            psycopg.connect(self.users_db_host, row_factory=dict_row) as con,  # ty: ignore[invalid-argument-type]
            con.cursor() as cur,
        ):
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
        Deletes a user by id.

        Parameters
        ----------
        user_id: UUID
            The id of the user to delete.
        """
        with (
            psycopg.connect(self.users_db_host, row_factory=dict_row) as con,  # ty: ignore[invalid-argument-type]
            con.cursor() as cur,
        ):
            cur.execute("DELETE FROM users WHERE id = %(id)s", {"id": user_id})
            con.commit()
