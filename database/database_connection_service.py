from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from database.models import Airport

class DatabaseConnectionService:
    def __init__(self, db_url: str):

        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

    def save_all_data(self):
        with self.connect() as connection:
            a = connection.query(Airport).all()
            print(a)
    # def query_airports(self, connection: ):

    @contextmanager
    def connect(self) -> Session:
        db = self.session()
        try:
            yield db
        finally:
            db.close()
