from utils.window_codes import WindowCodes


class GameData:

    opened_window: WindowCodes = WindowCodes.MAIN_MENU
    loaded_aircraft = []
    active_aircraft = []
    update_frequency: int = 0.3
    aircraft_generation_rate: float = 0.4
    total_active_aircraft: int = 1
    screen_speed_conversion_factor: float = 0.02
    percentage_outbound: float = 0.0
    airport: str = "LIS"
    airport_id: int = 1
