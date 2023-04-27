from database.data_management_service import DataManagementService
from windows.window_base import WindowBase
from utils.windows_parameters import SingleWindowParameters


class WindowMainMenu(WindowBase):
    def __init__(self, data_service: DataManagementService, win_parameters: SingleWindowParameters):
        super().__init__(data_service, win_parameters)

        self._create_window_elements()

        self.window.mainloop()

    def _create_window_elements(self):
        self._create_buttons(
            [
                {"master": self.window, "text": "New Game", "command": self._switch_to_game_window, "x": 0.2, "y": 0.4},
                {"master": self.window, "text": "Load Game", "command": self._close_window, "x": 0.3, "y": 0.5},
                {"master": self.window, "text": "Instructions Game", "command": self._close_window, "x": 0.4, "y": 0.6},
                {"master": self.window, "text": "Settings", "command": self._close_window, "x": 0.5, "y": 0.7},
                {"master": self.window, "text": "Exit Game", "command": self._exit_game, "x": 0.6, "y": 0.8}
            ]
        )
