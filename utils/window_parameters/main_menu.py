from utils.window_parameters.common import WindowParametersCommon
from utils.colours import Colours


class MainMenuWindowParametersBase(WindowParametersCommon):
    pass


class MainMenuWindowParameters(MainMenuWindowParametersBase):
    def __init__(self):
        self.title = "ATC Simulator"
        self.width = 0.5
        self.height = 0.7
        self.background_colour = Colours.DARK_GREY
        self.button_width = 0.25
        self.button_height = 0.1
        self.button_colour = Colours.LIGHT_GREY
        self.main_font = "Bahnschrift 2"
        self.button_font_colour = Colours.BLACK
