from utils.window_codes import WindowCodes


class GameData:

    opened_window: WindowCodes = WindowCodes.MAIN_MENU
    active_aircraft = {}
    update_frequency: int = 1
    aircraft_generation_rate: float = 0.4
    total_active_aircraft: int = 20
    screen_speed_conversion_factor: float = 0.02
    percentage_outbound: float = 0.5
    airport: str = "LIS"
    airport_id: int = 1

    def get_active_flight_numbers(self) -> list:
        return list(self.active_aircraft.keys())
