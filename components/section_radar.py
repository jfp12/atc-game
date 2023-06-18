from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from aircraft.aircraft_manager import AircraftManager
from components.map.map import Map
from components.log_list import LogList
from components.points_counter import PointsCounter


class SectionRadar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: GameDataManagementService):
        super().__init__(window, params, kwargs, data_service)

        self.aircraft_manager = None
        self.log_list = None
        self.points_counter = None
        self.map = Map.draw(self.canvas, self.width, self.height, self.data_service, self.params)

        self._initialize_log_list()
        self._initialize_aircraft_manager()
        self._initialize_point_counter()

    def _initialize_log_list(self):
        self.log_list = LogList(
            self.window,
            self.canvas,
            self.width,
            self.height,
            self.params,
            self.data_service,
        )

    def _initialize_aircraft_manager(self):
        self.aircraft_manager = AircraftManager(
            self.window,
            self.canvas,
            self.width,
            self.height,
            self.params,
            self.data_service,
            self.log_list
        )

    def _initialize_point_counter(self):
        self.points_counter = PointsCounter(
            self.window,
            self.canvas,
            self.width,
            self.height,
            self.params,
            self.data_service,
        )
