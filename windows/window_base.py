import tkinter as tk

from database.data_management_service import DataManagementService
from components.button import ButtonATC
from utils.windows_parameters import SingleWindowParameters


class WindowBase:
    def __init__(self, data_service: DataManagementService, win_parameters: SingleWindowParameters):

        self.parameters = data_service.get_parameters()
        self.params = win_parameters
        self.w_width = None
        self.w_height = None
        self.x_pos = None
        self.y_pos = None
        self.background = None
        self.window = None
        self.title = None

    def _setup_window(self):
        self.w_width = int(self.parameters.width_screen * self.params.width)
        self.w_height = int(self.parameters.height_screen * self.params.height)
        self.x_pos = int((1 - self.params.width) / 2 * self.parameters.width_screen)
        self.y_pos = int((1 - self.params.height) / 2 * self.parameters.height_screen)
        self.background = self.params.background_colour
        self.title = self.params.title

    def _open_window(self):
        self.window = tk.Tk()
        self.window.geometry(f"{self.w_width}x{self.w_height}+{self.x_pos}+{self.y_pos}")
        self.window.configure(bg=self.background)
        self.window.title(self.title)

    def _create_buttons(self, buttons: list):

        for button in buttons:
            button["master"] = self.window
            button["bg"] = self.params.button_colour
            button["fg"] = self.params.button_font_colour
            button["borderless"] = 1
            button["width"] = self.w_width * self.params.button_width
            button["height"] = self.w_height * self.params.button_height
            button["x"] = button["x"] * self.w_width
            button["y"] = button["y"] * self.w_height

            ButtonATC(button)

    def _close_window(self):
        self.window.destroy()
