from psycopg.abc import QueryNoTemplate
from psycopg_pool import ConnectionPool


class BasePostgresClient:
    """
    The base client for all Postgres databases.
    """

    def __init__(self, host: str, *, min_size: int = 1, max_size: int = 5):
        self._pool = ConnectionPool(host, min_size=min_size, max_size=max_size)

    def execute_query(self, query: QueryNoTemplate) -> list:
        with self._pool.connection() as con, con.cursor() as cur:
            cur.execute(query=query)
            rows = cur.fetchall() if cur.description else []
            con.commit()
        return rows

    def close_connection(self) -> None:
        self._pool.close()
