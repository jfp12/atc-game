from sqlalchemy import create_engine
from typing import List
from sqlalchemy.orm import sessionmaker, scoped_session, Session
import pandas as pd

from utils.window_codes import WindowCodes
from aircraft.aircraft import Aircraft


class GameData:
    opened_window: WindowCodes = WindowCodes.MAIN_MENU
    loaded_aircraft: List[Aircraft] = []
    active_aircraft: List[Aircraft] = []
    update_frequency: int = 1


class DataManagementService:
    def __init__(self, db_url: str = None):

        # Connection variables to data source
        self.db_url = None
        self.engine = None
        self.connection = None

        if db_url:
            self._setup_db_connection(db_url)
            self.start_db_connection()

        # Data variables
        self.airports = pd.DataFrame()
        self.runways = pd.DataFrame()
        self.flights = pd.DataFrame()
        self.waypoints = pd.DataFrame()

        # Game data variables
        self.game_data = GameData()

    def load_base_data(self):

        if self.db_url:
            self.db_save_all_airports()

    def db_save_all_airports(self):
        airports_df = pd.read_sql("SELECT * FROM AIRPORTS", self.engine, index_col=["id"])
        self.set_airports(airports_df)

    def _setup_db_connection(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)

    def start_db_connection(self):
        self.connection = self.engine.connect()

    def close_db_connection(self):
        self.connection = self.engine.connect().close()

    def set_airports(self, airports: pd.DataFrame):
        self.airports = airports

    def get_airports(self) -> pd.DataFrame:
        return self.airports
