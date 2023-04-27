from components.button import ButtonATC
from utils.windows_parameters import SingleWindowParameters
from database.data_management_service import DataManagementService
from utils.window_codes import WindowCodes


class Base:
    def __init__(
        self, window, width: float, height: float, params: SingleWindowParameters, data_service: DataManagementService
    ):
        self.data_service = data_service
        self.window = window
        self.width = width
        self.height = height
        self.params = params

        self.buttons = {}

    def _create_buttons(self, buttons: list):

        for button in buttons:
            button["bg"] = self.params.button_colour
            button["fg"] = self.params.button_font_colour
            button["borderless"] = 1
            button["width"] = self.width * self.params.button_width
            button["height"] = self.height * self.params.button_height
            button["x"] = button["x"] * self.width
            button["y"] = button["y"] * self.height

            self.buttons[button["text"]] = ButtonATC(button)

    def _switch_to_game_window(self):
        self.data_service.game_data.opened_window = WindowCodes.GAME
        self._close_window()

    def _exit_game(self):
        self.data_service.game_data.opened_window = WindowCodes.EXIT
        self._close_window()

    def _close_window(self):
        self.window.destroy()
