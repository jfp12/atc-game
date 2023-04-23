from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
import tkinter as tk
import pandas as pd

from database.models import Airport, Parameter


class Parameters:
    width_screen: float
    height_screen: float
    width_main_menu: float
    height_main_menu: float
    background_main_menu: str


class DataManagementService:
    def __init__(self, db_url: str = None):
        self.test = 1
        # Connection variables to data source
        self.db_url = None
        self.engine = None
        self.connection = None

        if db_url:
            self._setup_db_connection(db_url)
            self.start_db_connection()

        # Data variables
        self.parameters = Parameters()
        self.airports = pd.DataFrame()
        self.runways = pd.DataFrame()
        self.flights = pd.DataFrame()
        self.waypoints = pd.DataFrame()

    def load_base_data(self):

        if self.db_url:
            self.db_save_all_parameters()
            self.db_save_all_airports()

    def db_save_all_parameters(self):

        params_df = pd.read_sql(
            "SELECT * FROM PARAMETERS WHERE PARAMETERS.TYPE = 'dimension'", self.engine, index_col=["id"]
        )
        params_df["value"] = params_df["value"].astype(float)
        self.set_all_parameters(params_df)

        params_df = pd.read_sql(
            "SELECT * FROM PARAMETERS WHERE PARAMETERS.TYPE != 'dimension'", self.engine, index_col=["id"]
        )
        self.set_parameters(params_df)

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

    def set_screen_dimensions(self):
        root = tk.Tk()
        self.parameters.width_screen = root.winfo_screenwidth()
        self.parameters.height_screen = root.winfo_screenheight()
        root.destroy()

    def set_all_parameters(self, parameters: pd.DataFrame):
        self.set_parameters(parameters)
        self.set_screen_dimensions()

    def set_parameters(self, parameters: pd.DataFrame):
        for index, row in parameters.iterrows():
            setattr(self.parameters, row["name"], row["value"])

    def set_airports(self, airports: pd.DataFrame):
        self.airports = airports

    def get_parameters(self) -> Parameters:
        return self.parameters

    def get_airports(self) -> pd.DataFrame:
        return self.airports
