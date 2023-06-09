import random

import pandas as pd

from utils.game_data import GameData
from data_management.data_management_base import DataManagementBase


class GameDataManagementService(DataManagementBase):
    def __init__(self, db_url: str = None):

        if db_url:
            self._setup_db_connection(db_url)
            self.start_db_connection()

        # Data variables
        self.airports = pd.DataFrame()
        self.runways = {}
        self.flights = pd.DataFrame()
        self.waypoints = {}

        # Game data variables
        self.game_data = GameData()

    def load_base_data(self):

        if self.db_url:
            self._db_save_all_airports()
            self.load_game_data()

    def load_game_data(self):
        self._db_save_game_runways()
        self._db_save_game_waypoints()

    # Airport methods
    def _db_save_all_airports(self):
        airports_df = pd.read_sql("SELECT * FROM airports", self.engine)
        self.set_airports(airports_df)

    def set_airports(self, airports: pd.DataFrame):
        self.airports = airports

    def get_airports(self) -> pd.DataFrame:
        return self.airports

    def get_game_airport(self) -> pd.DataFrame:
        return self.airports[self.airports["code"] == self.game_data.airport].iloc[0]

    def get_game_airport_altitude(self) -> float:
        return self.get_game_airport()["altitude"]

    def get_game_airport_id(self) -> int:
        return self.get_game_airport()["id"]

    # Runway methods
    def _db_save_game_runways(self):
        runways_df = pd.read_sql(
            f"SELECT * FROM runways WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )
        self.set_game_runways(runways_df)

    def set_game_runways(self, runways: pd.DataFrame):
        from components.map.runway import MapRunway

        for index, runway in runways.iterrows():
            self.runways[runway["name"]] = MapRunway(runway)

    def get_game_runways(self) -> dict:
        return self.runways

    def get_random_game_runway_name(self) -> str:
        return random.choice(list(self.runways.keys()))

    def get_game_runway_x(self, runway: str) -> float:
        return self.runways[runway].get_x_init()

    def get_game_runway_y(self, runway: str) -> float:
        return self.runways[runway].get_y_initial()

    def get_game_runway_heading(self, runway: str) -> float:
        return self.runways[runway].get_heading()

    def get_game_waypoint_type(self, waypoint: str) -> str:
        return self.waypoints[waypoint].get_type()

    # Waypoint methods
    def _db_save_game_waypoints(self):
        waypoints_df = pd.read_sql(
            f"SELECT * FROM waypoints WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )
        self.set_game_waypoints(waypoints_df)

    def set_game_waypoints(self, waypoints: pd.DataFrame):
        from components.map import waypoints as waypoint_classes

        for index, waypoint in waypoints.iterrows():

            wpt_type = waypoint["type"]
            wpt_name = waypoint["name"]

            try:
                # Get waypoint class name from waypoint type
                class_name = f"Map{self._convert_name(wpt_type)}"

                # Try to initiate an object of the class determined above
                self.waypoints[wpt_name] = getattr(waypoint_classes, class_name)(waypoint)

            except AttributeError:
                raise AttributeError(f"Waypoint of type {wpt_type} is not recognized.")

    def get_game_waypoints(self) -> dict:
        return self.waypoints
