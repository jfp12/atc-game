from components.section_base import SectionBase
from data_management.game_data_service import GameDataService
from aircraft.aircraft_manager import AircraftManager
from components.map.map import Map
from components.log_list import LogList
from components.points_counter import PointsCounter


class SectionRadar(SectionBase):
    def __init__(self, window, kwargs, data: GameDataService, window_name: str):
        super().__init__(window, kwargs, data, window_name)

        self.aircraft_manager = None
        self.log_list = None
        self.points_counter = None
        self.map = Map.draw(self.canvas, self.width, self.height, self.data, self.p())

        self._initialize_log_list()
        self._initialize_aircraft_manager()
        self._initialize_point_counter()

    def _initialize_log_list(self):
        self.log_list = LogList(
            self.data,
            self.window_name,
            self.window,
            self.width,
            self.height,
            self.canvas
        )

    def _initialize_aircraft_manager(self):
        self.aircraft_manager = AircraftManager(
            self.data,
            self.window_name,
            self.window,
            self.width,
            self.height,
            self.canvas,
            self.log_list
        )

    def _initialize_point_counter(self):
        self.points_counter = PointsCounter(
            self.data,
            self.window_name,
            self.window,
            self.width,
            self.height,
            self.canvas
        )
