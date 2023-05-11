from sqlalchemy import create_engine
from typing import List
from sqlalchemy.orm import sessionmaker, scoped_session, Session
import pandas as pd
import random

from utils.window_codes import WindowCodes


class GameData:

    opened_window: WindowCodes = WindowCodes.MAIN_MENU
    loaded_aircraft = []
    active_aircraft = []
    update_frequency: int = 1
    aircraft_generation_rate: float = 0.4
    total_active_aircraft: int = 20
    screen_speed_conversion_factor: float = 0.02
    percentage_outbound: float = 0.5
    airport: str = "LIS"
    airport_id: int = 1


class Runway:
    def __init__(self, runway: pd.Series):
        self.name = runway["name"]
        self.length = runway["length"]
        self.heading = runway["heading"]
        self.x_init = runway["x_init"]
        self.y_init = runway["y_init"]
        self.active = runway["active"]

    def get_x(self) -> float:
        return self.x_init

    def get_y(self) -> float:
        return self.y_init

    def get_heading(self) -> float:
        return self.heading


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
        self.game_runways = {}
        self.flights = pd.DataFrame()
        self.waypoints = pd.DataFrame()

        # Game data variables
        self.game_data = GameData()

    def load_base_data(self):

        if self.db_url:
            self._db_save_all_airports()
            self.load_game_data()

    def load_game_data(self):
        self._db_save_game_runways()

    def _db_save_game_runways(self):
        runways_df = pd.read_sql(
            f"SELECT * FROM runways INNER JOIN runway_ends ON runways.id=runway_ends.runway_id WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )
        self.set_game_runways(runways_df)

    def _db_save_all_airports(self):
        airports_df = pd.read_sql("SELECT * FROM airports", self.engine)
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

    def set_game_runways(self, runways: pd.DataFrame):
        for index, runway in runways.iterrows():
            self.game_runways[runway["name"]] = Runway(runway)

    def get_airports(self) -> pd.DataFrame:
        return self.airports

    def get_game_airport(self) -> pd.DataFrame:
        return self.airports[self.airports["code"] == self.game_data.airport].iloc[0]

    def get_game_airport_altitude(self) -> float:
        return self.get_game_airport()["altitude"]

    def get_game_airport_id(self) -> int:
        return self.get_game_airport()["id"]

    def get_random_game_runway_name(self) -> str:
        return random.choice(list(self.game_runways.keys()))

    def get_game_runway_x(self, runway: str) -> float:
        return self.game_runways[runway].get_x()

    def get_game_runway_y(self, runway: str) -> float:
        return self.game_runways[runway].get_y()

    def get_game_runway_heading(self, runway: str) -> float:
        return self.game_runways[runway].get_heading()
