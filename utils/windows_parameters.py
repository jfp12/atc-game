from utils.colours import Colours


class SingleWindowParameters:
    title: str
    width: float
    height: float
    background_colour: str
    button_width: float
    button_height: float
    button_colour: str
    button_font: str
    button_font_colour: str


class WindowsParameters:
    def __init__(self):
        self.main = None
        self.game = None

        self._set_main_window()

    def _set_main_window(self):
        self.main = SingleWindowParameters()
        self.main.title = "ATC Simulator"
        self.main.width = 0.5
        self.main.height = 0.7
        self.main.background_colour = Colours.DARK_GREY
        self.main.button_width = 0.25
        self.main.button_height = 0.1
        self.main.button_colour = Colours.LIGHT_GREY
        self.main.button_font = "Bahnschrift 2"
        self.main.button_font_colour = Colours.BLACK
