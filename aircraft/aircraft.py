import math
import random
from typing import Tuple, Union

import numpy as np

from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService
from base import constants as c
from utils.colours import Colours as col


class Aircraft:
    data_service = None
    op_type = None
    runway = None

    def __init__(self, kwargs, canvas, data_service: GameDataManagementService, params: SingleWindowParameters, cmd_prompt):
        self.canvas = canvas
        self.data_service = data_service
        self.params = params

        # Unpack flight information
        self.flight_no = kwargs["flight_info"]["flight_no"]
        self.aircraft_type = kwargs["flight_info"]["aircraft_type"]
        self.aircraft_name = kwargs["flight_info"]["aircraft_name"]
        self.other_airport = kwargs["flight_info"]["other_airport"]
        self.other_airport_name = kwargs["flight_info"]["other_airport_name"]

        self.op_type = kwargs["op_type"]

        self.altitude = kwargs["alt"]
        self.tgt_altitude = kwargs["alt"]
        self.speed = kwargs["speed"]
        self.tgt_speed = kwargs["speed"]
        self.heading = kwargs["heading"]
        self.tgt_heading = kwargs["heading"]
        self.x = kwargs["x_init"]
        self.y = kwargs["y_init"]

        self.fill = kwargs["fill"]
        self.size = kwargs["size"]
        self.size_pos = kwargs["size_pos"]
        self.icon_id = None
        self.tag_id = None
        self.displacement_x = 0
        self.displacement_y = 0

        self.pos_history = []

        self._create_symbol()
        self._create_tag(cmd_prompt)

        # todo: import the variables below from somewhere else
        self.airport = "LIS"

        # self.aircraft = kwargs["aircraft"]
        # self.icon_id = kwargs["icon_id"]
        # self.tag_id = kwargs["tag_id"]
        # self.objective = kwargs["objective"]
        # self.collision = "black"
        # self.new_orange = False
        # self.new_red = False
        # self.visibility = visibility
        # self.moving = moving
        # self.on_ground = on_ground
        # self.points = 100
        # self.ils_status = "off"
        # self.ils_runway = None
        # self.distance_to_runway = 0
        # self.relative_angle_to_runway = 0
        # self.landing = False
        # self.previous_x = [-1] * 10
        # self.previous_y = [-1] * 10
        # self.last_pos_id = [-1] * 10
        # self.dep_wpt_x = dep_wpt_x
        # self.dep_wpt_y = dep_wpt_y

    # todo: create AircraftGenerator class and put there all generation things and call it from create class method
    @classmethod
    def create(cls, canvas, data_service: GameDataManagementService, width: float, height: float, params: SingleWindowParameters, cmd_prompt):
        cls.data_service = data_service
        cls.op_type = cls._compute_operation_type()
        cls.runway = cls._find_runway()
        x_init, y_init = cls._compute_initial_position()

        # Check first if there are available flights
        flight_info = cls._get_flight_information()

        if not flight_info:
            return

        # todo: change parameters to window parameter
        initial_state = {
            "op_type": cls.op_type,
            "flight_info": flight_info,
            "alt": cls._compute_initial_altitude(),
            "speed": cls._compute_initial_speed(),
            "x_init": x_init * width,
            "y_init": y_init * height,
            "heading": cls._compute_initial_heading(),
            "fill": col.BLACK,
            "size": 5,
            "size_pos": 1
        }

        return cls(initial_state, canvas, data_service, params, cmd_prompt)

    @classmethod
    def _compute_operation_type(cls) -> str:
        operation_type = random.uniform(0.0, 1.0)
        percentage_outbound = cls.data_service.game_data.percentage_outbound

        if operation_type <= percentage_outbound:
            return c.departure
        else:
            return c.arrival

    @classmethod
    def _compute_objective(cls, runway: str) -> str:
        if cls.op_type == c.departure:
            return "CHANGE"
        else:
            return runway

    @classmethod
    def _get_flight_information(cls) -> Union[dict, None]:
        return cls.data_service.fetch_flight_information_for_new_aircraft(cls.op_type)

    @classmethod
    def _compute_initial_altitude(cls) -> float:
        altitude = cls.data_service.get_game_airport_altitude()

        if cls.op_type == c.departure:
            return altitude
        else:
            return altitude + 1000 * random.randint(0, 2) + 6000

    @classmethod
    def _compute_initial_speed(cls) -> float:
        if cls.op_type == c.departure:
            return 0
        else:
            return 10 * random.randint(0, 2) + 240

    @classmethod
    def _compute_initial_heading(cls) -> float:
        if cls.op_type == c.departure:
            return cls.data_service.get_game_runway_heading(cls.runway)
        else:
            return 180

    @classmethod
    def _find_runway(cls) -> str:
        return cls.data_service.get_random_game_runway_name()

    @classmethod
    def _compute_initial_position(cls) -> Tuple[float, float]:

        if cls.op_type == c.departure:
            return cls.data_service.get_game_runway_x(cls.runway), cls.data_service.get_game_runway_y(cls.runway)
        else:
            return 0.3, 0.3

    def _create_symbol(self):
        self.icon_id = self.canvas.create_rectangle(
            self.x-self.size,
            self.y-self.size,
            self.x+self.size,
            self.y+self.size,
            fill=self.fill,
            outline=self.fill
        )

    def _create_tag(self, cmd_prompt):
        # Create tag
        self.tag_id = self.canvas.create_text(
            self.x - 23,
            self.y - 20,
            fill=self.fill,
            font="Arial 10",
            text=self._get_tag_text()
        )

        def _add_callsign_to_prompt(event, flight_no, prompt):
            prompt.delete(0, 'end')
            prompt.insert(0, f"{flight_no} ")

        # todo: improve, see suggestion
        eval_label = lambda x, y, z: (lambda p: _add_callsign_to_prompt(x, y, z))
        self.canvas.tag_bind(self.tag_id, "<Button-1>", eval_label(self, self.flight_no, cmd_prompt))

    def process_altitude_request(self, new_altitude: str):
        new_altitude = int(new_altitude)

        self.tgt_altitude = new_altitude

    def process_heading_request(self, new_heading: str):
        new_heading = int(new_heading)

        self.tgt_heading = new_heading

    def process_speed_request(self, new_speed: str):
        new_speed = int(new_speed)

        self.tgt_speed = new_speed

    def update(self):
        self._update_state_variables()
        self._update_aircraft_position()
        self._update_positions_history()
        self._update_tag_text()

        self._move()

    def _update_state_variables(self):
        self._update_altitude()
        self._update_heading()
        self._update_speed()

    def _update_altitude(self):
        # Get altitude difference
        altitude_diff = self.tgt_altitude - self.altitude

        # Update altitude
        self.altitude += np.sign(altitude_diff) * min(self.params.rate_change_altitude, abs(altitude_diff))

    def _update_heading(self):
        # Get heading difference
        heading_diff = self.tgt_heading - self.heading

        # Get sign correction for cases in which the aircraft might take the longer turn
        sign_correction = 1 if abs(heading_diff) <= 180 else -1

        # Update heading
        self.heading += (
            sign_correction *
            np.sign(heading_diff) *
            min(self.params.rate_change_heading, abs(heading_diff))
        )

        # Keep heading always between 1 and 360
        self.heading = self.heading % 360
        self.heading = (not self.heading) * 360 + self.heading

    def _update_speed(self):
        # Get speed difference
        speed_diff = self.tgt_speed - self.speed

        # Update speed
        self.speed += np.sign(speed_diff) * min(self.params.rate_change_speed, abs(speed_diff))

    def _update_aircraft_position(self):
        self._compute_displacement()
        self._compute_new_position()

    def _update_positions_history(self):
        self._push_position_to_history()
        self._delete_position_from_history()

    def _push_position_to_history(self):
        self.pos_history.append(self._create_old_position())

    def _delete_position_from_history(self):
        if len(self.pos_history) > self.params.aircraft_max_pos_history:
            self.canvas.delete(self.pos_history.pop(0))

    def _create_old_position(self):
        return self.canvas.create_rectangle(
            self.x - self.size_pos,
            self.y - self.size_pos,
            self.x + self.size_pos,
            self.y + self.size_pos,
            fill=self.fill,
            outline=self.fill
        )

    def _compute_displacement(self):
        self.displacement_x = self._get_speed_on_screen() * math.sin(math.pi * self.heading / 180.0)
        self.displacement_y = - self._get_speed_on_screen() * math.cos(math.pi * self.heading / 180.0)

    def _compute_new_position(self):
        self.x += self.displacement_x
        self.y += self.displacement_y

    def _move(self):
        self.canvas.move(self.icon_id, self.displacement_x, self.displacement_y)
        self.canvas.move(self.tag_id, self.displacement_x, self.displacement_y)

    def _get_speed_on_screen(self) -> float:
        return self.speed * self.data_service.game_data.screen_speed_conversion_factor

    def _update_tag_text(self):
        self.canvas.itemconfigure(self.tag_id, text=self._get_tag_text(), fill=self.fill)

    def _get_tag_text(self) -> str:
        return (
            f"{self.flight_no}\n" +
            f"{self.aircraft_type}\n" +
            f"{self.other_airport}\n" +
            f"{str(int(self.altitude))} {str(int(self.tgt_altitude))}\n" +
            f"{str(int(self.speed))} {str(int(self.tgt_speed))}\n"
            f"{str(int(self.heading))} {str(int(self.tgt_heading))}"
        )
