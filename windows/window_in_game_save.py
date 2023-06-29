from windows.window_base import WindowBase
from data_management.game_data_service import GameDataService
from components.section_in_game_save import SectionInGameSave
from components.section_footer import SectionFooter


class WindowInGameSave(WindowBase):
    def __init__(self, data: GameDataService):
        super().__init__(data, self.__class__.__name__)

        self._open_canvas()

        self._create_window_elements()

    def _create_window_elements(self):
        self._create_sections(
            [
                {
                    "name": SectionInGameSave.__name__, "bg": self.p().body_background_colour,
                    "width": self.width * self.p().body_width, "height": self.height * self.p().body_height,
                    "x": self.width * self.p().body_x, "y": self.height * self.p().body_y
                },
                {
                    "name": SectionFooter.__name__, "bg": self.p().footer_background_colour,
                    "width": self.width * self.p().footer_width, "height": self.height * self.p().footer_height,
                    "x": self.width * self.p().footer_x, "y": self.height * self.p().footer_y
                },
            ]
        )
