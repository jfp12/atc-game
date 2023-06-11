from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from aircraft.aircraft_manager import AircraftManager
from components.map.map import Map


class SectionRadar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: GameDataManagementService):
        super().__init__(window, params, kwargs, data_service)

        self.aircraft_manager = None
        self.map = Map.draw(self.canvas, self.width, self.height, self.data_service, self.params)

        self._initialize_aircraft_manager(kwargs["cmd_prompt"])

    def _initialize_aircraft_manager(self, cmd_prompt):
        self.aircraft_manager = AircraftManager(
            self.window,
            self.canvas,
            self.width,
            self.height,
            self.params,
            self.data_service,
            cmd_prompt
        )
