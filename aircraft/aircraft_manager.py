from typing import List
import random
import math

from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from aircraft.aircraft import Aircraft
from base.base import Base


class AircraftManager(Base):
    def __init__(
            self, window, canvas, width, height, params: SingleWindowParameters, data_service: GameDataManagementService
    ):
        super().__init__(window, width, height, params, data_service, canvas)

        self.aircraft_list = []

        self._load_aircraft(self.data_service.game_data.loaded_aircraft)

    def _load_aircraft(self, active_aircraft: List[Aircraft]):
        pass

    def create_aircraft(self):

        if self._is_aircraft_generated():
            self.data_service.game_data.active_aircraft.append(
                Aircraft.create(self.canvas, self.data_service, self.width, self.height)
            )

    def move_aircraft(self):
        aircraft: Aircraft
        for aircraft in self.data_service.game_data.active_aircraft:
            aircraft.update()

    def _is_aircraft_generated(self) -> bool:
        creation = random.uniform(0.0, 1.0)

        if (
            self._get_creation_probability() < creation or
            self._get_number_active_aircraft() >= self.data_service.game_data.total_active_aircraft
        ):
            return False
        else:
            return True

    def _get_creation_probability(self):
        constant = self.data_service.game_data.aircraft_generation_rate
        number = self._get_number_active_aircraft()
        return math.exp(- constant * number)

    def _get_number_active_aircraft(self):
        return len(self.data_service.game_data.active_aircraft)
