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
                {"master": self.section, "text": "Pause Game", "command": self._exit_game, "x": 0, "y": 0.73,
                 "width": self.params.sidebar_button_width, "height": self.params.sidebar_button_height},
                {"master": self.section, "text": "Save Game", "command": self._exit_game, "x": 0, "y": 0.78,
                 "width": self.params.sidebar_button_width, "height": self.params.sidebar_button_height},
                {"master": self.section, "text": "Exit to Main Menu", "command": self._switch_to_main_menu_window, "x": 0, "y": 0.83,
                 "width": self.params.sidebar_button_width, "height": self.params.sidebar_button_height},
                {"master": self.section, "text": "Exit Game", "command": self._exit_game, "x": 0, "y": 0.88,
                 "width": self.params.sidebar_button_width, "height": self.params.sidebar_button_height}
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
