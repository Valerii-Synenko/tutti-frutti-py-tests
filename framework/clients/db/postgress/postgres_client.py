from psycopg_pool import ConnectionPool


class PostgresClient:
    """
    The base client for all Postgres databases.
    """

    def __init__(self, host: str, *, min_size: int = 1, max_size: int = 5):
        self._pool = ConnectionPool(host, min_size=min_size, max_size=max_size)

    def close_connection(self) -> None:
        self._pool.close()
