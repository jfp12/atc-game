from typing import List
import random
import math

from data_management.game_data_management_service import GameDataManagementService
from aircraft.aircraft import Aircraft
from base.base import Base
from components.log_list import LogList


class AircraftManager(Base):
    def __init__(
            self, data: GameDataManagementService, window_name, window, width, height, canvas, log_list: LogList
    ):
        super().__init__(data, window_name, window, width, height, canvas)

        self.log_list = log_list

        self.aircraft_list = []

    def create_aircraft(self, cmd_prompt):

        if self._is_aircraft_generated():
            new_aircraft = Aircraft.create(
                self.canvas, self.data, self.width, self.height, cmd_prompt, self.log_list, self.window_name
            )

            if new_aircraft:
                self.data.game_data.active_aircraft[new_aircraft.flight_no] = new_aircraft

    def move_aircraft(self):
        for aircraft in self.data.game_data.active_aircraft.values():
            aircraft.update()

    def hand_aircraft_over(self):
        to_hand_over = []
        active_aircraft = self.data.game_data.active_aircraft

        # Identify which aircraft should be removed
        for aircraft in active_aircraft.values():
            if aircraft.to_be_hand_over:
                to_hand_over.append(aircraft.flight_no)

        # Remove the aircraft identified
        for hand_over in to_hand_over:
            active_aircraft[hand_over].remove_aircraft_from_radar()

    def _is_aircraft_generated(self) -> bool:
        creation = random.uniform(0.0, 1.0)

        if (
            self._get_creation_probability() < creation or
            self._get_number_active_aircraft() >= self.data.game_data.total_active_aircraft
        ):
            return False
        else:
            return True

    def _get_creation_probability(self):
        constant = self.data.game_data.aircraft_generation_rate
        number = self._get_number_active_aircraft()
        return math.exp(- constant * number)

    def _get_number_active_aircraft(self):
        return len(self.data.game_data.active_aircraft)
