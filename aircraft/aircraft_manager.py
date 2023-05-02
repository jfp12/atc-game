from typing import List
import random
import math

from utils.windows_parameters import SingleWindowParameters
from database.data_management_service import DataManagementService
from aircraft.aircraft import Aircraft
from base.base import Base


class AircraftManager(Base):
    def __init__(
            self, window, canvas, width, height, params: SingleWindowParameters, data_service: DataManagementService
    ):
        super().__init__(window, width, height, params, data_service, canvas)

        self.aircraft_list = []

        self._load_aircraft(self.data_service.game_data.loaded_aircraft)

    def _load_aircraft(self, active_aircraft: List[Aircraft]):
        pass

    def create_aircraft(self):
        self._is_aircraft_generated()

        # kwargs = {
        #     "x": 0.5 * self.width,
        #     "y": 0.5 * self.height,
        #     "fill": self.params.aircraft_symbol_colour,
        #     "size": self.params.aircraft_symbol_size,
        #     "speed": 10,
        #     "heading": 1
        # }
        # self.data_service.game_data.active_aircraft.append(Aircraft(kwargs, self.canvas))

    def move_aircraft(self):
        aircraft: Aircraft
        for aircraft in self.data_service.game_data.active_aircraft:
            aircraft.update()

    def _is_aircraft_generated(self):
        creation = random.uniform(0.0, 1.0)

        if (
            self._get_creation_probability() < creation or
            self._get_active_aircraft() >= self.data_service.game_data.total_active_aircraft
        ):
            return

        self.data_service.game_data.active_aircraft.append(Aircraft.create(self.canvas, self.data_service))

    def _get_creation_probability(self):
        constant = self.data_service.game_data.aircraft_generation_rate
        number = self._get_active_aircraft()
        return math.exp(- constant * number)

    def _get_active_aircraft(self):
        return len(self.data_service.game_data.active_aircraft)
