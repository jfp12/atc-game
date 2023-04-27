from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from database.data_management_service import DataManagementService
from components.aircraft_list import AircraftList


class SectionSidebar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: DataManagementService):
        super().__init__(window, params, kwargs, data_service)

        self._create_sidebar_elements()

    def _create_sidebar_elements(self):
        self._create_aircraft_list()

        self._create_buttons(
            [
                {"master": self.section, "text": "Exit Game", "command": self._exit_game, "x": 0.6, "y": 0.8}
            ]
        )

    def _create_aircraft_list(self):
        AircraftList(
            width=self.width,
            height=self.height,
            window=self.section,
            canvas=self.canvas,
            bg=self.params.aircraft_list_colour,
            params=self.params
        )
