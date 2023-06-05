from re import sub

from sqlalchemy import create_engine


class DataManagementBase:
    db_url = None
    engine = None
    connection = None

    def _setup_db_connection(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def start_db_connection(self):
        self.connection = self.engine.connect()

    def close_db_connection(self):
        self.connection.close()

    @staticmethod
    def _convert_name(name: str) -> str:
        return sub(r"(-)+", " ", name).title().replace(" ", "")
