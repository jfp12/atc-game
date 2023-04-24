from database.data_management_service import DataManagementService
from windows.window_base import WindowBase
from utils.windows_parameters import SingleWindowParameters


class WindowMainMenu(WindowBase):
    def __init__(self, data_service: DataManagementService, win_parameters: SingleWindowParameters):
        super().__init__(data_service, win_parameters)

        self._setup_window()
        self._open_window()
        self._create_buttons(
            [
                {"text": "Exit Game", "command": self._close_window, "x": 0.2, "y": 0.4},
                {"text": "Exit Game", "command": self._close_window, "x": 0.3, "y": 0.5},
                {"text": "Exit Game", "command": self._close_window, "x": 0.4, "y": 0.6},
                {"text": "Exit Game", "command": self._close_window, "x": 0.5, "y": 0.7}
            ]
        )
        self.window.mainloop()
