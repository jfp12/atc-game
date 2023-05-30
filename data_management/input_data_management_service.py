from urllib.parse import urlparse
from pathlib import Path

import pandas as pd

from data_management import models
from data_management.data_management_base import DataManagementBase


class InputDataManagementService(DataManagementBase):
    def __init__(self, input_url: str, db_url: str):
        self.input_url = None
        self.db_url = None

        self._prepare_input_url(input_url)
        self._setup_db_connection(db_url)
        self.start_db_connection()

    def _prepare_input_url(self, input_url: str):
        parsed_input_url = self._parse_url(input_url, types_url=["file"], full_url=False)[1:]

        self.input_url = Path(__file__).parents[1] / parsed_input_url

        if not self.input_url.exists():
            raise NotADirectoryError(f"Could not find directory {self.input_url}")

    def _parse_url(self, input_url: str, types_url: list[str], full_url: bool = True):
        parsed_url = urlparse(input_url)

        if parsed_url.scheme not in types_url:
            raise ValueError(f"Storage URL scheme {parsed_url.scheme} is invalid. Expected {types_url}.")

        if full_url:
            return parsed_url
        else:
            return parsed_url.path

    def load_file(self, filename: str, tablename: str):
        full_path = Path(__file__).parent / f"{self.input_url}/{filename}"

        if not full_path.exists():
            raise FileNotFoundError(f"Could not find file {full_path}.")

        if tablename not in self._get_db_tablenames():
            raise ValueError(f"Name {tablename} is not an expected table name in the database.")

        data = pd.read_csv(full_path)

        getattr(self, f"load_{tablename}")(data)

        self.connection.commit()

    def load_airports(self, data: pd.DataFrame):
        data.to_sql(models.Airport.__tablename__, self.connection, if_exists="append", index=False)

    def load_runways(self, data: pd.DataFrame):
        airports = pd.read_sql("SELECT id, code FROM AIRPORTS", self.connection)

        data = pd.merge(data, airports, on="code")

        # Get dataframe in right format
        data = data.rename(columns={"id": "airport_id"}).drop(columns="code")
        data["heading"] = data["heading"].astype(float)
        data["name"] = data["name"].astype(str).str.zfill(2)

        data.to_sql(models.Runway.__tablename__, self.connection, if_exists="append", index=False)

        self.connection.commit()

    def load_waypoints(self, data: pd.DataFrame):
        airports = pd.read_sql("SELECT id, code FROM AIRPORTS", self.connection)

        data = pd.merge(data, airports, on="code")
        data = data.rename(columns={"id": "airport_id"}).drop(columns="code")

        data.to_sql(models.Waypoint.__tablename__, self.connection, if_exists="append", index=False)

    @staticmethod
    def _get_db_tablenames() -> list[str]:
        return [
            models.Airport.__tablename__,
            models.Flight.__tablename__,
            models.Waypoint.__tablename__,
            models.Parameter.__tablename__,
            models.Runway.__tablename__
        ]
