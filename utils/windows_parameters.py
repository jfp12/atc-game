from utils.colours import Colours


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

    radar_width: float = None
    radar_height: float = None

    sidebar_colour: str = None
    sidebar_button_width: float = None
    sidebar_button_height: float = None

    aircraft_list_colour: str = None
    aircraft_list_width: float = None
    aircraft_list_height: float = None
    aircraft_list_x0: float = None
    aircraft_list_y0: float = None
    aircraft_list_title: str = None
    aircraft_list_title_x0: float = None
    aircraft_list_title_y0: float = None
    aircraft_list_departure_colour: str = None
    aircraft_list_departure_text: str = None
    aircraft_list_arrival_colour: str = None
    aircraft_list_arrival_text: str = None
    aircraft_list_font_title_size: float = None
    aircraft_list_font_text_size: float = None
    aircraft_list_font_colour: str = None

    aircraft_symbol_colour: str = None
    aircraft_symbol_size: float = None

    cmd_prompt_title: str = None
    cmd_prompt_title_font_size: float = None
    cmd_prompt_title_font_colour: str = None
    cmd_prompt_title_x0: float = None
    cmd_prompt_title_y0: float = None
    cmd_prompt_input_font_size: float = None
    cmd_prompt_input_x0: float = None
    cmd_prompt_input_y0: float = None
    cmd_prompt_input_width: int = None
    cmd_prompt_x0: float = None
    cmd_prompt_y0: float = None
    cmd_prompt_x1: float = None
    cmd_prompt_y1: float = None


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
        self.main.background_colour = Colours.DARK_GREY
        self.main.button_width = 0.25
        self.main.button_height = 0.1
        self.main.button_colour = Colours.LIGHT_GREY
        self.main.main_font = "Bahnschrift 2"
        self.main.button_font_colour = Colours.BLACK

    def _set_game_window(self):
        self.game = SingleWindowParameters()
        self.game.title = "Game"
        self.game.width = 1
        self.game.height = 1
        self.game.background_colour = Colours.DARK_BLUE
        self.game.button_width = 0.25
        self.game.button_height = 0.1
        self.game.button_colour = Colours.LIGHT_GREY
        self.game.main_font = "Bahnschrift"
        self.game.button_font_colour = Colours.BLACK
        self.game.radar_width = 0.8
        self.game.radar_height = 1
        self.game.sidebar_colour = Colours.WHITE
        self.game.sidebar_button_width = 1
        self.game.sidebar_button_height = 0.05
        self.game.aircraft_list_colour = Colours.DARK_GREY
        self.game.aircraft_list_width = 0.85
        self.game.aircraft_list_height = 0.5
        self.game.aircraft_list_x0 = 0.05
        self.game.aircraft_list_y0 = 0.05
        self.game.aircraft_list_title = "Active Flights List"
        self.game.aircraft_list_title_x0 = 0.55
        self.game.aircraft_list_title_y0 = 0.06
        self.game.aircraft_list_departure_colour = Colours.LIGHT_BLUE
        self.game.aircraft_list_departure_text = "Dep.:"
        self.game.aircraft_list_arrival_colour = Colours.LIGHT_YELLOW
        self.game.aircraft_list_departure_text = "Arr.:"
        self.game.aircraft_symbol_colour = Colours.BLACK
        self.game.aircraft_list_font_title_size = 0.1
        self.game.aircraft_list_font_text_size = 0.05
        self.game.aircraft_list_font_colour = Colours.BLACK
        self.game.aircraft_symbol_size = 5
        self.game.cmd_prompt_title = "ATC Commands"
        self.game.cmd_prompt_title_font_size = 0.05
        self.game.cmd_prompt_title_font_colour = Colours.WHITE
        self.game.cmd_prompt_title_x0 = 0.5
        self.game.cmd_prompt_title_y0 = 0.585
        self.game.cmd_prompt_input_font_size = 0.05
        self.game.cmd_prompt_input_x0 = 0.1
        self.game.cmd_prompt_input_y0 = 0.595
        self.game.cmd_prompt_input_width = 22
        self.game.cmd_prompt_x0 = 0.05
        self.game.cmd_prompt_y0 = 0.57
        self.game.cmd_prompt_x1 = 0.92
        self.game.cmd_prompt_y1 = 0.64
