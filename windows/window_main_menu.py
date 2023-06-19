from windows.window_base import WindowBase
from data_management.game_data_management_service import GameDataManagementService


class WindowMainMenu(WindowBase):

    def __init__(self, data: GameDataManagementService):
        super().__init__(data, self.__class__.__name__)

        self._create_window_elements()
        self.window.mainloop()

    def _create_window_elements(self):
        self._create_buttons(
            [
                {"master": self.window, "text": "New Game", "command": self._switch_to_game_window, "x": 0.2, "y": 0.4,
                 "width": self.p().button_width, "height": self.p().button_height},
                {"master": self.window, "text": "Load Game", "command": self._close_window, "x": 0.3, "y": 0.5,
                 "width": self.p().button_width, "height": self.p().button_height},
                {"master": self.window, "text": "Instructions Game", "command": self._close_window, "x": 0.4, "y": 0.6,
                 "width": self.p().button_width, "height": self.p().button_height},
                {"master": self.window, "text": "Settings", "command": self._close_window, "x": 0.5, "y": 0.7,
                 "width": self.p().button_width, "height": self.p().button_height},
                {"master": self.window, "text": "Exit Game", "command": self._exit_game, "x": 0.6, "y": 0.8,
                 "width": self.p().button_width, "height": self.p().button_height}
            ]
        )
