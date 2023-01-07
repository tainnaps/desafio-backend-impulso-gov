from sqlite3 import Connection, connect

DEFAULT_DATABASE = "dados.db"


class EstablishmentModel:
    def _connect_to_sqlite(self, db_name=DEFAULT_DATABASE) -> Connection:
        return connect(db_name)

    def get_all_by_city_id(
        self, city_id: int, db_name=DEFAULT_DATABASE
    ) -> list[list]:
        query = """--sql
            SELECT id_cnes, nome, latitude, longitude
            FROM estabelecimentos
            WHERE municipio_id_sus=?
            """

        with self._connect_to_sqlite(db_name) as con:
            establishments = con.cursor().execute(query, (city_id,)).fetchall()

        return establishments

    def get_by_cnes_id(self, cnes_id: int, db_name=DEFAULT_DATABASE) -> list:
        query = """--sql
            SELECT id_cnes, nome, latitude, longitude
            FROM estabelecimentos
            WHERE id_cnes=?
            """

        with self._connect_to_sqlite(db_name) as con:
            establishment = con.cursor().execute(query, (cnes_id,)).fetchone()

        return establishment
