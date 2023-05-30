import random

import pandas as pd

from utils.game_data import GameData
from data_management.data_management_base import DataManagementBase


class Runway:
    def __init__(self, runway: pd.Series):
        self.name = runway["name"]
        self.length = runway["length"]
        self.heading = runway["heading"]
        self.x_init = runway["x_init"]
        self.y_init = runway["y_init"]

    def get_x(self) -> float:
        return self.x_init

    def get_y(self) -> float:
        return self.y_init

    def get_heading(self) -> float:
        return self.heading


class Waypoint:
    def __init__(self, waypoint: pd.Series):
        pass


class GameDataManagementService(DataManagementBase):
    def __init__(self, db_url: str = None):

        if db_url:
            self._setup_db_connection(db_url)
            self.start_db_connection()

        # Data variables
        self.airports = pd.DataFrame()
        self.runways = {}
        self.flights = pd.DataFrame()
        self.waypoints = pd.DataFrame()

        # Game data variables
        self.game_data = GameData()

    def load_base_data(self):

        if self.db_url:
            self._db_save_all_airports()
            self.load_game_data()

    def _db_save_all_airports(self):
        airports_df = pd.read_sql("SELECT * FROM airports", self.engine)
        self.set_airports(airports_df)

    def load_game_data(self):
        self._db_save_game_runways()

    def _db_save_game_runways(self):
        runways_df = pd.read_sql(
            f"SELECT * FROM runways WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )
        self.set_game_runways(runways_df)

    def _db_save_game_waypoints(self):
        waypoints_df = pd.read_sql(
            f"SELECT * FROM waypoints WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )

    def set_airports(self, airports: pd.DataFrame):
        self.airports = airports

    def set_game_runways(self, runways: pd.DataFrame):
        for index, runway in runways.iterrows():
            self.runways[runway["name"]] = Runway(runway)

    def set_game_waypoints(self, waypoints: pd.DataFrame):
        for index, waypoint in waypoints.iterrows():
            self.waypoints[waypoint["name"]] = Waypoint(waypoint)

    def get_airports(self) -> pd.DataFrame:
        return self.airports

    def get_game_airport(self) -> pd.DataFrame:
        return self.airports[self.airports["code"] == self.game_data.airport].iloc[0]

    def get_game_airport_altitude(self) -> float:
        return self.get_game_airport()["altitude"]

    def get_game_airport_id(self) -> int:
        return self.get_game_airport()["id"]

    def get_random_game_runway_name(self) -> str:
        return random.choice(list(self.runways.keys()))

    def get_game_runway_x(self, runway: str) -> float:
        return self.runways[runway].get_x()

    def get_game_runway_y(self, runway: str) -> float:
        return self.runways[runway].get_y()

    def get_game_runway_heading(self, runway: str) -> float:
        return self.runways[runway].get_heading()
