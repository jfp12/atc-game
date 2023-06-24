from utils.window_parameters.common import WindowParametersCommon
from utils.colours import Colours


class GameWindowParametersBase(WindowParametersCommon):
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


class GameWindowParameters(GameWindowParametersBase):
    def __init__(self):
        self.title = "Game"
        self.width = 1
        self.height = 0.95
        self.background_colour = Colours.DARK_BLUE
        self.button_width = 0.25
        self.button_height = 0.1
        self.button_colour = Colours.LIGHT_GREY
        self.main_font = "Bahnschrift"
        self.button_font_colour = Colours.BLACK
        self.radar_width = 0.8
        self.radar_height = 1
        self.sidebar_colour = Colours.WHITE
        self.sidebar_button_width = 1
        self.sidebar_button_height = 0.05
        self.aircraft_list_colour = Colours.DARK_GREY
        self.aircraft_list_width = 0.85
        self.aircraft_list_height = 0.5
        self.aircraft_list_x0 = 0.05
        self.aircraft_list_y0 = 0.05
        self.aircraft_list_title = "Active Flights List"
        self.aircraft_list_title_x0 = 0.5
        self.aircraft_list_title_y0 = 0.03
        self.aircraft_list_departure_colour = Colours.LIGHT_BLUE
        self.aircraft_list_departure_text = "Dep.:"
        self.aircraft_list_arrival_colour = Colours.LIGHT_YELLOW
        self.aircraft_list_arrival_text = "Arr.:"
        self.aircraft_list_ils_on = "ILS {rwy}"
        self.aircraft_list_ils_intercept = "ILS {rwy} INT"
        self.aircraft_symbol_colour = Colours.BLACK
        self.aircraft_list_font_title_size = 0.09
        self.aircraft_list_font_text_size = 0.037
        self.aircraft_list_font_colour = Colours.BLACK
        self.aircraft_symbol_size = 5
        self.aircraft_max_pos_history = 10
        self.aircraft_default_points = 100
        self.cmd_prompt_title = "ATC Commands"
        self.cmd_prompt_title_font_size = 0.05
        self.cmd_prompt_title_font_colour = Colours.WHITE
        self.cmd_prompt_title_x0 = 0.5
        self.cmd_prompt_title_y0 = 0.585
        self.cmd_prompt_input_font_size = 0.05
        self.cmd_prompt_input_x0 = 0.1
        self.cmd_prompt_input_y0 = 0.595
        self.cmd_prompt_input_width = 22
        self.cmd_prompt_x0 = 0.05
        self.cmd_prompt_y0 = 0.57
        self.cmd_prompt_x1 = 0.92
        self.cmd_prompt_y1 = 0.64
        self.wpt_colour = Colours.WHITE
        self.wpt_size = 0.02
        self.rwy_colour = Colours.WHITE
        self.actions = {
            "altitude": ["a", "alt", "altitude"],
            "heading": ["h", "hdg", "heading"],
            "speed": ["s", "spd", "speed"],
            "takeoff": ["t", "to", "takeoff", "take-off"],
            "lineup": ["lu", "line-up", "lineup"],
            "ils": ["ils"],
            "landing_clearance": ["l", "land"]
        }
        self.min_altitude = 100
        self.min_altitude_landing = 150
        self.max_altitude = 40000
        self.min_heading = 1
        self.max_heading = 360
        self.init_heading_variation = 30
        self.min_speed = 150
        self.max_speed = 500
        self.min_distance_landing_runway = 0.05
        self.rate_change_altitude = 200
        self.rate_change_heading = 3
        self.rate_change_speed = 15
        self.ils_gs_max_altitude = 3000
        self.ils_loc_angular_range = 18
        self.ils_loc_range = 0.2
        self.ils_loc_angle_intercept = 90
        self.ils_angle_gain = 15
        self.map_spawn_x = [0.01, 0.5, 0.99]
        self.map_spawn_y = [0.01, 0.5, 0.99]
        self.obj_dep_min_distance = 0.05
        self.obj_dep_min_altitude = 5000
        self.day_periods = {
            "0": {"h": [0, 5], "t": "night"},
            "1": {"h": [6, 11], "t": "morning"},
            "2": {"h": [12, 17], "t": "afternoon"},
            "3": {"h": [18, 21], "t": "evening"},
            "4": {"h": [22, 23], "t": "night"},
        }
        self.log_list_font_size = 13
        self.log_list_max = 20
        self.log_list_duration = 5
        self.log_list_vertical_spacing = 0.03
        self.log_list_x0 = 0.01
        self.log_list_y0 = 0.02
        self.log_list_info_colour = Colours.WHITE
        self.log_list_success_colour = Colours.GREEN
        self.log_list_warn_colour = Colours.ORANGE
        self.log_list_foul_colour = Colours.RED
        self.log_list_msg_dep_ready = "{flight_no}: Good {period}, holding short of runway {rwy}."
        self.log_list_dep_takeoff_invalid_spd_hdg = "{flight_no}: Cannot take-off, we don't have a speed and heading clearance."
        self.log_list_msg_arr_ready = "{flight_no}: Good {period}, with you at {alt}ft, heading {hdg}."
        self.point_counter_x0 = 1
        self.point_counter_y0 = 0.02
        self.point_counter_colour = Colours.BLACK
        self.point_counter_font_size = 15
        self.point_counter_text = "Points: {points}"
