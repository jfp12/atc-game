from components.button import ButtonATC
from data_management.game_data_service import GameDataService


class Base:
    def __init__(
        self, data: GameDataService, window_name, window=None, width: float = None, height: float = None, canvas=None
    ):
        self.window_name = window_name

        self.data = data
        self.window = window
        self.canvas = canvas
        self.width = width
        self.height = height

        self.buttons = {}

    def _set_width(self, width: float):
        self.width = width

    def _set_height(self, height: float):
        self.height = height

    def _set_window(self, window):
        self.window = window

    def _set_canvas(self, canvas):
        self.canvas = canvas

    def p(self):
        return self.data.parameters[self.window_name]

    def _create_buttons(self, buttons: list):

        for button in buttons:
            button["bg"] = self.p().button_colour
            button["fg"] = self.p().button_font_colour
            button["borderless"] = 1
            button["width"] = self.width * button["width"]
            button["height"] = self.height * button["height"]
            button["x"] = button["x"] * self.width
            button["y"] = button["y"] * self.height

            self.buttons[button["text"]] = ButtonATC(button)

    def _calculate_font_size(self, font_size: float) -> str:
        return str(int(font_size * self.width))

    def _switch_to_game_window(self):
        self.data.game_data.opened_window = self.data.window_codes.GAME
        self._close_window()

    def _switch_to_main_menu_window(self):
        self.data.game_data.opened_window = self.data.window_codes.MAIN_MENU
        self._close_window()

    def _open_in_game_save_window(self):
        from windows.window_in_game_save import WindowInGameSave

        self.data.game_data.paused = True
        WindowInGameSave(self.data)

    def _exit_game(self):
        self.data.game_data.opened_window = self.data.window_codes.EXIT
        self._close_window()

    def _close_window(self):
        self.window.destroy()
