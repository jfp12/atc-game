import random
from typing import Union

import pandas as pd

from data_management.data_management_base import DataManagementBase
import base.constants as c
from utils.window_parameters import (
    MainMenuWindowParameters,
    GameWindowParameters,
    InGameSaveWindowParameters
)
from utils.window_codes import WindowCodes
from utils.game_data import GameData


class GameDataService(DataManagementBase):
    def __init__(self, db_url: str = None):

        if db_url:
            self._setup_db_connection(db_url)
            self.start_db_connection()

        # Data variables
        self.airports = pd.DataFrame()
        self.arrivals = pd.DataFrame()
        self.departures = pd.DataFrame()
        self.runways = {}
        self.waypoints = {}

        # Initialize window codes
        self.window_codes = WindowCodes()

        # Game data variables
        self.game_data = GameData(self.window_codes.MAIN_MENU)

        # Windows parameters
        self.parameters = {
            self.window_codes.MAIN_MENU: MainMenuWindowParameters(),
            self.window_codes.GAME: GameWindowParameters(),
            self.window_codes.IN_GAME_SAVE: InGameSaveWindowParameters()
        }

    def load_base_data(self):

        if self.db_url:
            self._db_save_all_airports()
            self.load_game_data()

    def load_game_data(self):
        self._db_save_game_runways()
        self._db_save_game_waypoints()
        self._db_save_game_flights()

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

    def get_game_active_runway(self):
        return self.runways["05"]

    def get_random_game_runway_name(self) -> str:
        return random.choice(list(self.runways.keys()))

    # Waypoint methods
    def _db_save_game_waypoints(self):
        waypoints_df = pd.read_sql(
            f"SELECT * FROM waypoints WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )
        self.set_game_waypoints(waypoints_df)

    def set_game_waypoints(self, waypoints: pd.DataFrame):
        from components.map import waypoint as waypoint_classes

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

    def get_game_random_waypoint(self):
        return random.choice(list(self.waypoints.values()))

    def get_game_waypoint_type(self, waypoint: str) -> str:
        return self.waypoints[waypoint].get_type()

    # Flights methods
    def _db_save_game_flights(self):
        flight_df = pd.read_sql(
            f"SELECT * FROM flights WHERE airport_id = {self.get_game_airport_id()}", self.engine
        )
        self.set_game_flights(flight_df)

    def set_game_flights(self, flights: pd.DataFrame):
        self.arrivals = flights[flights["bound"] == c.arrival]
        self.departures = flights[flights["bound"] == c.departure]

    def fetch_flight_information_for_new_aircraft(self, bound: str) -> Union[dict, None]:
        flights_df = self.arrivals if bound == c.arrival else self.departures

        # If there are no available flights, return empty dictionary
        try:
            return self.filter_flights_on_active_flight_numbers(flights_df).sample().iloc[0].to_dict()
        except ValueError:
            return None

    def filter_flights_on_active_flight_numbers(self, flights_df: pd.DataFrame) -> pd.DataFrame:
        return flights_df[~flights_df["flight_no"].isin(self.game_data.get_active_flight_numbers())]
