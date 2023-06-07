from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from components.aircraft_list import AircraftList
from components.command_prompt import CommandPrompt


class SectionSidebar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: GameDataManagementService):
        super().__init__(window, params, kwargs, data_service)

        self.aircraft_list = None
        self.command_prompt = None

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

        self._create_command_prompt()

    def _create_aircraft_list(self):
        self.aircraft_list = AircraftList(
            data_service=self.data_service,
            width=self.width,
            height=self.height,
            window=self.section,
            canvas=self.canvas,
            bg=self.params.aircraft_list_colour,
            params=self.params
        )

    def _create_command_prompt(self):
        self.command_prompt = CommandPrompt(
            self.canvas,
            self.width,
            self.height,
            self.params,
            self.data_service
        )
