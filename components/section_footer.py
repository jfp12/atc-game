from components.section_base import SectionBase
from data_management.game_data_service import GameDataService


class SectionFooter(SectionBase):
    def __init__(self, window, kwargs, data: GameDataService, window_name: str):
        super().__init__(window, kwargs, data, window_name)

        self._create_footer_elements()

    def _create_footer_elements(self):

        self._create_buttons(
            [
                {
                    "master": self.section,
                    "text": self.p().footer_button_save_text,
                    "command": self._close_window,
                    "x": self.p().footer_button_save_x,
                    "y": self.p().footer_button_save_y,
                    "width": self.p().footer_button_width,
                    "height": self.p().footer_button_height},
                {
                    "master": self.section,
                    "text": self.p().footer_button_cancel_text,
                    "command": self._close_window,
                    "x": self.p().footer_button_cancel_x,
                    "y": self.p().footer_button_cancel_y,
                    "width": self.p().footer_button_width,
                    "height": self.p().footer_button_height}
            ]
        )
