import tkinter as tk

from database.data_management_service import DataManagementService
from components.button import ATCButton


class WindowBase:
    def __init__(self, data_service: DataManagementService):

        self.parameters = data_service.get_parameters()

        self.w_width = None
        self.w_height = None
        self.x_pos = None
        self.y_pos = None
        self.background = None
        self.window = None
        self.title = None

    def _setup_window(self, title: str, width: float, height: float, background: str):
        self.w_width = int(self.parameters.width_screen * width)
        self.w_height = int(self.parameters.height_screen * height)
        self.x_pos = int((1 - width) / 2 * self.parameters.width_screen)
        self.y_pos = int((1 - height) / 2 * self.parameters.height_screen)
        self.background = f"#{background}"
        self.title = title

    def _open_window(self):
        self.window = tk.Tk()
        self.window.geometry(f"{self.w_width}x{self.w_height}+{self.x_pos}+{self.y_pos}")
        self.window.configure(bg=self.background)
        self.window.title(self.title)

    def _create_buttons(self, buttons: list):

        for button in buttons:
            ATCButton(button)
