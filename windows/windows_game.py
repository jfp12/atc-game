from datetime import datetime, timedelta

from data_management.game_data_management_service import GameDataManagementService
from windows.window_base import WindowBase
from utils.windows_parameters import SingleWindowParameters
from components.section_radar import SectionRadar
from components.section_sidebar import SectionSidebar
from utils.window_codes import WindowCodes


class WindowGame(WindowBase):
    def __init__(self, data_service: GameDataManagementService, win_parameters: SingleWindowParameters):
        super().__init__(data_service, win_parameters)

        self.r_width = None
        self.r_height = None
        self.step = datetime.utcnow()
        self.aircraft_manager = None

        self._open_canvas()
        self._set_radar_dimensions()
        self._create_window_elements()
        self._run_game()
        self.window.mainloop()

    def _run_game(self):
        update_freq = timedelta(seconds=self.data_service.game_data.update_frequency)

        while self.data_service.game_data.opened_window == WindowCodes.GAME:

            if (datetime.utcnow() - self.step) > update_freq:
                self._update()
                self._update_game_step()

            self.window.update()

        self.window.mainloop()

    def _update(self):
        self.sections[SectionRadar.__name__].aircraft_manager.create_aircraft()

        self.sections[SectionRadar.__name__].aircraft_manager.move_aircraft()

        self.sections[SectionSidebar.__name__].aircraft_list.add_aircraft_to_list()

    def _create_window_elements(self):
        self._create_sections(
            [
                {
                    "name": SectionSidebar.__name__, "bg": self.params.sidebar_colour,
                    "width": (self.w_width - self.r_width), "height": self.r_height, "x": self.r_width, "y": 0
                }
            ]
        )
        self._create_sections(
            [
                {
                    "name": SectionRadar.__name__, "bg": self.params.background_colour, "width": self.r_width,
                    "height": self.r_height, "x": 0, "y": 0, "cmd_prompt": self._get_command_prompt_object()
                }
            ]
        )

    def _set_radar_dimensions(self):
        self.r_width = int(self.w_width * self.params.radar_width)
        self.r_height = int(self.w_height * self.params.radar_height)

    def _update_game_step(self):
        self.step = datetime.utcnow()

    def _get_command_prompt_object(self):
        return self.sections[SectionSidebar.__name__].command_prompt.prompt
