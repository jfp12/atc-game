import math
import random
from typing import Tuple

from data_management.game_data_management_service import GameDataManagementService
from base import constants as c
from utils.colours import Colours as col


class Aircraft:
    data_service = None
    op_type = None
    runway = None

    def __init__(self, kwargs, canvas, data_service: GameDataManagementService):
        self.canvas = canvas
        self.data_service = data_service

        # self.flight_no = kwargs["flight_no"]
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
        self.icon_id = None
        self.tag_id = None
        self.displacement_x = 0
        self.displacement_y = 0

        self._create_symbol()
        self._create_tag()

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
    def create(cls, canvas, data_service: GameDataManagementService, width: float, height: float):
        cls.data_service = data_service
        cls.op_type = cls._compute_operation_type()
        cls.runway = cls._find_runway()

        x_init, y_init = cls._compute_initial_position()

        initial_state = {
            "op_type": cls.op_type,
            "alt": cls._compute_initial_altitude(),
            "speed": cls._compute_initial_speed(),
            "x_init": x_init * width,
            "y_init": y_init * height,
            "heading": cls._compute_initial_heading(),
            # todo: change fill to window parameter
            "fill": col.BLACK,
            "size": 5
        }

        return cls(initial_state, canvas, data_service)

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
            return 360

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

    def _create_tag(self):
        self.tag_id = self.canvas.create_text(
            self.x-23,
            self.y-20,
            fill=self.fill,
            font="Arial 10",
            text=self._get_tag_text()
        )

        # eval_label = lambda x, y, z: (lambda p: self.add_callsign_to_prompt(x, y, z))
        # game_vars.canvas.tag_bind(tag_id, "<Button-1>", eval_label(self, self.flight_no, cmd_prompt))

    def update(self):
        self._update_state_variables()
        self._update_tag_text()

        self._move()

    def _update_state_variables(self):
        self._compute_displacement()
        self._compute_new_position()

    def _update_tag_text(self):
        self.canvas.itemconfigure(self.tag_id, text=self._get_tag_text(), fill=self.fill)

    def _compute_displacement(self):
        self.displacement_x = self._get_speed_on_screen() * math.sin(math.pi * self.heading / 180.0)
        self.displacement_y = self._get_speed_on_screen() * math.cos(math.pi * self.heading / 180.0)

    def _compute_new_position(self):
        self.x += self.displacement_x
        self.y += self.displacement_y

    def _move(self):
        self.canvas.move(self.icon_id, self.displacement_x, self.displacement_y)
        self.canvas.move(self.tag_id, self.displacement_x, self.displacement_y)

    def _get_speed_on_screen(self) -> float:
        return self.speed * self.data_service.game_data.screen_speed_conversion_factor

    def _get_tag_text(self) -> str:
        return (
            f"FLIGHT_NO\n" +
            f"AIRCRAFT\n" +
            f"AIRPORT\n" +
            f"{str(int(self.altitude))} {str(int(self.tgt_altitude))}\n" +
            f"{str(int(self.speed))} {str(int(self.tgt_speed))}"
        )
