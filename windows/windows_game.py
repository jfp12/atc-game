from datetime import datetime, timedelta

from data_management.game_data_service import GameDataService
from windows.window_base import WindowBase
from components.section_radar import SectionRadar
from components.section_sidebar import SectionSidebar


class WindowGame(WindowBase):
    def __init__(self, data: GameDataService):
        super().__init__(data, self.__class__.__name__)

        self.r_width = None
        self.r_height = None

        self.aircraft_manager = None

        self.step = datetime.utcnow()

        # todo: move it to WindowBase, which implies adding sections to all windows
        self._open_canvas()

        self._set_radar_dimensions()
        self._create_window_elements()

        self._run_game()

        self.window.mainloop()

    def _run_game(self):
        update_freq = timedelta(seconds=self.data.game_data.update_frequency)

        while self.data.game_data.opened_window == self.data.window_codes.GAME:
            if not self.data.game_data.paused:

                if (datetime.utcnow() - self.step) > update_freq:
                    self._update()
                    self._update_game_step()

            self.window.update()

        self.window.mainloop()

    def _update(self):
        self.sections[SectionRadar.__name__].aircraft_manager.create_aircraft(
            self._get_command_prompt_object_from_sidebar(),
        )

        self.sections[SectionRadar.__name__].aircraft_manager.move_aircraft()

        self.sections[SectionRadar.__name__].aircraft_manager.hand_aircraft_over()

        self.sections[SectionSidebar.__name__].aircraft_list.add_aircraft_to_list()

        self.sections[SectionRadar.__name__].log_list.delete_expired_logs()

        self.sections[SectionRadar.__name__].points_counter.update_text()

    def _create_window_elements(self):
        self._create_sections(
            [
                {
                    "name": SectionSidebar.__name__, "bg": self.p().sidebar_colour,
                    "width": (self.width - self.r_width), "height": self.r_height, "x": self.r_width, "y": 0
                },
            ]
        )
        self._create_sections(
            [
                {
                    "name": SectionRadar.__name__, "bg": self.p().background_colour, "width": self.r_width,
                    "height": self.r_height, "x": 0, "y": 0
                }
            ]
        )

    def _set_radar_dimensions(self):
        self.r_width = int(self.width * self.p().radar_width)
        self.r_height = int(self.height * self.p().radar_height)

    def _update_game_step(self):
        self.step = datetime.utcnow()

    def _get_command_prompt_object_from_sidebar(self):
        return self.sections[SectionSidebar.__name__].command_prompt.prompt

    def _get_log_list_object_from_radar(self):
        return self.sections[SectionRadar.__name__].log_list
