from utils.window_codes import WindowCodes


class GameData:

    opened_window: WindowCodes = WindowCodes.MAIN_MENU
    game_points = 0
    active_aircraft = {}
    update_frequency: int = 0.3
    aircraft_generation_rate: float = 0.4
    total_active_aircraft: int = 10
    screen_speed_conversion_factor: float = 0.02
    percentage_outbound: float = 0
    airport: str = "LIS"
    airport_id: int = 1

    def get_active_flight_numbers(self) -> list:
        return list(self.active_aircraft.keys())

    def add_to_game_points(self, points: int):
        self.game_points += points

    def remove_from_active_aircraft(self, flight_no: str):
        del self.active_aircraft[flight_no]
