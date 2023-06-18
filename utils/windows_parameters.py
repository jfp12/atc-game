from typing import List

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
    aircraft_list_ils_on: str = None
    aircraft_list_ils_intercept: str = None
    aircraft_list_font_title_size: float = None
    aircraft_list_font_text_size: float = None
    aircraft_list_font_colour: str = None

    aircraft_symbol_colour: str = None
    aircraft_symbol_size: float = None
    aircraft_max_pos_history: int = None
    aircraft_default_points: int = None

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

    wpt_colour: str = None
    wpt_size: float = None
    rwy_colour: str = None

    actions: dict = None
    min_altitude: float = None
    min_altitude_landing: float = None
    max_altitude: float = None
    min_heading: float = None
    max_heading: float = None
    init_heading_variation: float = None
    min_speed: float = None
    max_speed: float = None
    min_distance_landing_runway: float = None
    rate_change_altitude: float = None
    rate_change_heading: float = None
    rate_change_speed: float = None
    ils_gs_max_altitude: float = None
    ils_loc_angular_range: float = None
    ils_loc_range: float = None
    ils_loc_angle_intercept: float = None
    ils_angle_gain: float = None

    map_spawn_x: list = None
    map_spawn_y: list = None

    obj_dep_min_distance: float = None
    obj_dep_min_altitude: float = None

    day_periods: dict = None

    log_list_font_size: int = None
    log_list_max: int = None
    log_list_duration: int = None
    log_list_vertical_spacing: float = None
    log_list_x0: float = None
    log_list_y0: float = None
    log_list_info_colour: str = None
    log_list_success_colour: str = None
    log_list_warn_colour: str = None
    log_list_foul_colour: str = None
    log_list_msg_dep_ready: str = None
    log_list_dep_takeoff_invalid_spd_hdg: str = None
    log_list_msg_arr_ready: str = None

    point_counter_x0: float = None
    point_counter_y0: float = None
    point_counter_colour: str = None
    point_counter_font_size: float = None
    point_counter_text: str = None


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
        self.game.aircraft_list_arrival_text = "Arr.:"
        self.game.aircraft_list_ils_on = "ILS {rwy}"
        self.game.aircraft_list_ils_intercept = "ILS {rwy} INT"
        self.game.aircraft_symbol_colour = Colours.BLACK
        self.game.aircraft_list_font_title_size = 0.1
        self.game.aircraft_list_font_text_size = 0.05
        self.game.aircraft_list_font_colour = Colours.BLACK
        self.game.aircraft_symbol_size = 5
        self.game.aircraft_max_pos_history = 10
        self.game.aircraft_default_points = 100
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
        self.game.wpt_colour = Colours.WHITE
        self.game.wpt_size = 0.02
        self.game.rwy_colour = Colours.WHITE
        self.game.actions = {
            "altitude": ["a", "alt", "altitude"],
            "heading": ["h", "hdg", "heading"],
            "speed": ["s", "spd", "speed"],
            "takeoff": ["t", "to", "takeoff", "take-off"],
            "lineup": ["lu", "line-up", "lineup"],
            "ils": ["ils"],
            "landing_clearance": ["l", "land"]
        }
        self.game.min_altitude = 100
        self.game.min_altitude_landing = 150
        self.game.max_altitude = 40000
        self.game.min_heading = 1
        self.game.max_heading = 360
        self.game.init_heading_variation = 30
        self.game.min_speed = 150
        self.game.max_speed = 500
        self.game.min_distance_landing_runway = 0.05
        self.game.rate_change_altitude = 200
        self.game.rate_change_heading = 3
        self.game.rate_change_speed = 15
        self.game.ils_gs_max_altitude = 3000
        self.game.ils_loc_angular_range = 18
        self.game.ils_loc_range = 0.2
        self.game.ils_loc_angle_intercept = 90
        self.game.ils_angle_gain = 15
        self.game.map_spawn_x = [0.01, 0.5, 0.99]
        self.game.map_spawn_y = [0.01, 0.5, 0.99]
        self.game.obj_dep_min_distance = 0.05
        self.game.obj_dep_min_altitude = 5000

        self.game.day_periods = {
            "0": {"h": [0, 5], "t": "night"},
            "1": {"h": [6, 11], "t": "morning"},
            "2": {"h": [12, 17], "t": "afternoon"},
            "3": {"h": [18, 21], "t": "evening"},
            "4": {"h": [22, 23], "t": "night"},
        }

        self.game.log_list_font_size = 13
        self.game.log_list_max = 20
        self.game.log_list_duration = 5
        self.game.log_list_vertical_spacing = 0.03
        self.game.log_list_x0 = 0.01
        self.game.log_list_y0 = 0.02
        self.game.log_list_info_colour = Colours.WHITE
        self.game.log_list_success_colour = Colours.GREEN
        self.game.log_list_warn_colour = Colours.ORANGE
        self.game.log_list_foul_colour = Colours.RED
        self.game.log_list_msg_dep_ready = "{flight_no}: Good {period}, holding short of runway {rwy}."
        self.game.log_list_dep_takeoff_invalid_spd_hdg = "{flight_no}: Cannot take-off, we don't have a speed and heading clearance."
        self.game.log_list_msg_arr_ready = "{flight_no}: Good {period}, with you at {alt}ft, heading {hdg}."

        self.game.point_counter_x0 = 1
        self.game.point_counter_y0 = 0.02
        self.game.point_counter_colour = Colours.BLACK
        self.game.point_counter_font_size = 15
        self.game.point_counter_text = "Points: {points}"
