import pymssql

class ConnectionPool:
    def __init__(self, server, user, password, database, minconn=1, maxconn=10):
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.minconn = minconn
        self.maxconn = maxconn
        self._pool = []

    def connect(self):
        for _ in range(self.minconn):
            conn = self._create_connection()
            self._pool.append(conn)

    def _create_connection(self):
        return pymssql.connect(
            server=self.server,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def acquire(self):
        if not self._pool:
            self.connect()
        return self._pool.pop()

    def release(self, conn):
        self._pool.append(conn)

def create_pool(server, user, password, database, minconn=1, maxconn=10):
    pool = ConnectionPool(server, user, password, database, minconn=minconn, maxconn=maxconn)
    pool.connect()
    return pool
