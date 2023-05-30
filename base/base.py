from components.button import ButtonATC
from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from utils.window_codes import WindowCodes


class Base:
    def __init__(
        self, window, width: float, height: float, params: SingleWindowParameters, data_service: GameDataManagementService, canvas = None
    ):
        self.data_service = data_service
        self.window = window
        self.canvas = canvas
        self.width = width
        self.height = height
        self.params = params

        self.buttons = {}

    def _create_buttons(self, buttons: list):

        for button in buttons:
            button["bg"] = self.params.button_colour
            button["fg"] = self.params.button_font_colour
            button["borderless"] = 1
            button["width"] = self.width * button["width"]
            button["height"] = self.height * button["height"]
            button["x"] = button["x"] * self.width
            button["y"] = button["y"] * self.height

            self.buttons[button["text"]] = ButtonATC(button)

    def _calculate_font_size(self, font_size: float) -> str:
        return str(int(font_size * self.width))

    def _switch_to_game_window(self):
        self.data_service.game_data.opened_window = WindowCodes.GAME
        self._close_window()

    def _switch_to_main_menu_window(self):
        self.data_service.game_data.opened_window = WindowCodes.MAIN_MENU
        self._close_window()

    def _exit_game(self):
        self.data_service.game_data.opened_window = WindowCodes.EXIT
        self._close_window()

    def _close_window(self):
        self.window.destroy()
