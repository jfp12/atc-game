from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from aircraft.aircraft_manager import AircraftManager


class SectionRadar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: GameDataManagementService):
        super().__init__(window, params, kwargs, data_service)

        self.aircraft_manager = None
        self.map = map

        self._initialize_aircraft_manager()

    def _initialize_aircraft_manager(self):
        self.aircraft_manager = AircraftManager(
            self.window,
            self.canvas,
            self.width,
            self.height,
            self.params,
            self.data_service
        )
