from components.section_base import SectionBase
from data_management.game_data_service import GameDataService
from components.aircraft_list import AircraftList
from components.command_prompt import CommandPrompt


class SectionSidebar(SectionBase):
    def __init__(self, window, kwargs, data: GameDataService, window_name: str):
        super().__init__(window, kwargs, data, window_name)

        self.aircraft_list = None
        self.command_prompt = None

        self._create_sidebar_elements()

    def _create_sidebar_elements(self):

        self._create_buttons(
            [
                {"master": self.section, "text": "Pause Game", "command": self._exit_game, "x": 0, "y": 0.78,
                 "width": self.p().sidebar_button_width, "height": self.p().sidebar_button_height},
                {"master": self.section, "text": "Save Game", "command": self._open_in_game_save_window, "x": 0,
                 "y": 0.83, "width": self.p().sidebar_button_width, "height": self.p().sidebar_button_height},
                {"master": self.section, "text": "Exit to Main Menu", "command": self._switch_to_main_menu_window,
                 "x": 0, "y": 0.88, "width": self.p().sidebar_button_width,
                 "height": self.p().sidebar_button_height},
                {"master": self.section, "text": "Exit Game", "command": self._exit_game, "x": 0, "y": 0.93,
                 "width": self.p().sidebar_button_width, "height": self.p().sidebar_button_height}
            ]
        )

        self._create_command_prompt()
        self._create_aircraft_list()

    def _create_aircraft_list(self):
        self.aircraft_list = AircraftList(
            data=self.data,
            window_name=self.window_name,
            window=self.section,
            width=self.width,
            height=self.height,
            canvas=self.canvas,
            bg=self.p().aircraft_list_colour,
            cmd_prompt=self.command_prompt.prompt
        )

    def _create_command_prompt(self):
        self.command_prompt = CommandPrompt(
            self.canvas,
            self.width,
            self.height,
            self.data,
            self.p()
        )
