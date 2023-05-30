from data_management.game_data_management_service import GameDataManagementService
from windows.window_base import WindowBase
from utils.windows_parameters import SingleWindowParameters


class WindowMainMenu(WindowBase):
    def __init__(self, data_service: GameDataManagementService, win_parameters: SingleWindowParameters):
        super().__init__(data_service, win_parameters)

        self._create_window_elements()
        self.window.mainloop()

    def _create_window_elements(self):
        self._create_buttons(
            [
                {"master": self.window, "text": "New Game", "command": self._switch_to_game_window, "x": 0.2, "y": 0.4,
                 "width": self.params.button_width, "height": self.params.button_height},
                {"master": self.window, "text": "Load Game", "command": self._close_window, "x": 0.3, "y": 0.5,
                 "width": self.params.button_width, "height": self.params.button_height},
                {"master": self.window, "text": "Instructions Game", "command": self._close_window, "x": 0.4, "y": 0.6,
                 "width": self.params.button_width, "height": self.params.button_height},
                {"master": self.window, "text": "Settings", "command": self._close_window, "x": 0.5, "y": 0.7,
                 "width": self.params.button_width, "height": self.params.button_height},
                {"master": self.window, "text": "Exit Game", "command": self._exit_game, "x": 0.6, "y": 0.8,
                 "width": self.params.button_width, "height": self.params.button_height}
            ]
        )
