from sqlite3 import Connection, connect


class EstablishmentModel:
    def _connect_to_sqlite(self, db_name="dados.db") -> Connection:
        return connect(db_name)
