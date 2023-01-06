from sqlite3 import Connection, connect


class EstablishmentModel:
    def _connect_to_sqlite(self, db_name="dados.db") -> Connection:
        return connect(db_name)

    def get_all_by_city_id(self, city_id: int) -> list[list]:
        query = """--sql
            SELECT id_cnes, nome, latitude, longitude
            FROM estabelecimentos
            WHERE municipio_id_sus=?
            """

        with self._connect_to_sqlite() as con:
            establishments = con.cursor().execute(query, (city_id,)).fetchall()

        return establishments

