import tkinter as tk

from database.data_management_service import DataManagementService
from windows.window_base import WindowBase
from components.button import ATCButtonCreate


class WindowMainMenu(WindowBase):
    def __init__(self, data_service: DataManagementService):
        super().__init__(data_service)

        self._setup_window(
            title="ATC Simulator",
            width=self.parameters.width_main_menu,
            height=self.parameters.height_main_menu,
            background=self.parameters.background_main_menu
        )
        self._open_window()
        self._create_buttons(
            [
                {"master": self.window, "text": "Exit Game", "command": self.window.destroy}
            ]
        )
        self.window.mainloop()
