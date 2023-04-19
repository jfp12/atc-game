from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnectionService:
    def __init__(self, db_url: str):

        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
