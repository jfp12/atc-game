from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from database.data_management_service import DataManagementService
from aircraft.aircraft_manager import AircraftManager


class SectionRadar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: DataManagementService):
        super().__init__(window, params, kwargs, data_service)

        self.aircraft_manager = None

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
