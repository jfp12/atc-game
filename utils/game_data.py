class GameData:
    def __init__(self, initial_window: str):
        self.opened_window = initial_window
        self.paused = False
        self. game_points = 0
        self.active_aircraft = {}
        self.update_frequency: int = 0.3
        self.aircraft_generation_rate: float = 0.4
        self.total_active_aircraft: int = 10
        self.screen_speed_conversion_factor: float = 0.02
        self.percentage_outbound: float = 0
        self.airport: str = "LIS"
        self.airport_id: int = 1

    def get_active_flight_numbers(self) -> list:
        return list(self.active_aircraft.keys())

    def add_to_game_points(self, points: int):
        self.game_points += points

    def remove_from_active_aircraft(self, flight_no: str):
        del self.active_aircraft[flight_no]
