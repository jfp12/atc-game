from utils.colours import Colours as c


class SingleWindowParameters:
    main_font: str = None
    title: str = None
    width: float = None
    height: float = None
    background_colour: str = None
    button_width: float = None
    button_height: float = None
    button_colour: str = None
    button_font_colour: str = None
    radar_width: str = None
    radar_height: str = None
    sidebar_colour: str = None
    aircraft_list_colour: str = None
    aircraft_list_width: float = None
    aircraft_list_height: float = None
    aircraft_list_x0: float = None
    aircraft_list_y0: float = None
    aircraft_list_title: float = None


class WindowsParameters:
    def __init__(self):
        self.main = None
        self.game = None

        self._set_main_window()
        self._set_game_window()

    def _set_main_window(self):
        self.main = SingleWindowParameters()
        self.main.title = "ATC Simulator"
        self.main.width = 0.5
        self.main.height = 0.7
        self.main.background_colour = c.DARK_GREY
        self.main.button_width = 0.25
        self.main.button_height = 0.1
        self.main.button_colour = c.LIGHT_GREY
        self.main.main_font = "Bahnschrift 2"
        self.main.button_font_colour = c.BLACK

    def _set_game_window(self):
        self.game = SingleWindowParameters()
        self.game.title = "Game"
        self.game.width = 1
        self.game.height = 1
        self.game.background_colour = c.DARK_BLUE
        self.game.button_width = 0.25
        self.game.button_height = 0.1
        self.game.button_colour = c.LIGHT_GREY
        self.game.main_font = "Bahnschrift 50"
        self.game.button_font_colour = c.BLACK
        self.game.radar_width = 0.8
        self.game.radar_height = 1
        self.game.sidebar_colour = c.WHITE
        self.game.aircraft_list_colour = c.DARK_GREY
        self.game.aircraft_list_width = 0.85
        self.game.aircraft_list_height = 0.5
        self.game.aircraft_list_x0 = 0.05
        self.game.aircraft_list_y0 = 0.05
        self.game.aircraft_list_title = "Active Flights List"
