import math
import random
from typing import Tuple, Union

import numpy as np
from shapely.geometry import Point

from data_management.game_data_management_service import GameDataManagementService
from utils.colours import Colours as col
from base import constants as c
from components.map.runway import MapRunway
from components.map.waypoint import MapWaypoint
from components.log_list import LogList


class Aircraft:
    data = None
    op_type = None
    runway = None
    waypoint = None
    params = None

    cmd_prompt = None
    log_list = None

    def __init__(
        self,
        kwargs,
        canvas,
        data: GameDataManagementService,
        width: float
    ):
        self.canvas = canvas
        self.data = data
        self.width = width

        # Unpack flight information
        self.flight_no = kwargs["flight_info"]["flight_no"]
        self.aircraft_type = kwargs["flight_info"]["aircraft_type"]
        self.aircraft_name = kwargs["flight_info"]["aircraft_name"]
        self.other_airport = kwargs["flight_info"]["other_airport"]
        self.other_airport_name = kwargs["flight_info"]["other_airport_name"]

        self.op_type = kwargs["op_type"]
        self.objective = kwargs["objective"]
        self.objective_name = self.objective.get_name()

        self.altitude = kwargs["alt"]
        self.tgt_altitude = kwargs["alt"]
        self.speed = kwargs["speed"]
        self.tgt_speed = kwargs["speed"]
        self.heading = kwargs["heading"]
        self.tgt_heading = kwargs["heading"]
        self.x = kwargs["x_init"]
        self.y = kwargs["y_init"]

        # Aircraft status (flight progress)
        self.phase = c.taxi if self.op_type == c.departure else c.airborne
        self.to_be_hand_over = False

        self.fill = kwargs["fill"]
        self.size = kwargs["size"]
        self.size_pos = kwargs["size_pos"]

        self.icon_id = None
        self.tag_id = None

        self.displacement_x = 0
        self.displacement_y = 0
        self.pos_history = []

        self.points = self.params.aircraft_default_points

        # todo: import the variables below from somewhere else
        self.airport = "LIS"

        self._create_symbol_on_map()

        self.log_list.add_log({"aircraft": self, "type": c.dep_ready if self.op_type == c.departure else c.arr_ready})

        # self.collision = "black"
        # self.new_orange = False
        # self.new_red = False
        # self.moving = moving
        # self.on_ground = on_ground
        # self.points = 100
        # self.ils_status = "off"
        # self.ils_runway = None
        # self.distance_to_runway = 0
        # self.relative_angle_to_runway = 0
        # self.landing = False
        # self.dep_wpt_x = dep_wpt_x
        # self.dep_wpt_y = dep_wpt_y

    # todo: create AircraftGenerator class and put there all generation things and call it from create class method
    @classmethod
    def create(
            cls,
            canvas,
            data: GameDataManagementService,
            width: float,
            height: float,
            cmd_prompt,
            log_list: LogList,
            window_name
    ):
        cls.cmd_prompt = cmd_prompt
        cls.log_list = log_list

        cls.params = data.parameters[window_name]
        cls.data = data
        cls.op_type = cls._compute_operation_type()
        cls.runway = cls._find_runway()
        # todo: departures also have a waypoint for now
        cls.waypoint = cls._find_waypoint()
        x_init, y_init = cls._compute_initial_position(width, height)

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
            "x_init": x_init,
            "y_init": y_init,
            "heading": cls._compute_initial_heading(x_init, y_init),
            "objective": cls._compute_objective(),
            "fill": col.BLACK,
            "size": 5,
            "size_pos": 1
        }

        return cls(initial_state, canvas, data, width)

    @classmethod
    def _compute_operation_type(cls) -> str:
        operation_type = random.uniform(0.0, 1.0)
        percentage_outbound = cls.data.game_data.percentage_outbound

        if operation_type <= percentage_outbound:
            return c.departure
        else:
            return c.arrival

    @classmethod
    def _compute_objective(cls) -> Union[MapRunway, MapWaypoint]:
        if cls.op_type == c.departure:
            return cls.waypoint
        else:
            return cls.runway

    @classmethod
    def _compute_initial_position(cls, width: float, height: float) -> Tuple[float, float]:

        if cls.op_type == c.departure:
            return cls.runway.get_x_init(), cls.runway.get_y_init()
        else:
            return cls._get_coordinates_initial_for_arrival(width, height)

    @classmethod
    def _get_coordinates_initial_for_arrival(cls, width: float, height: float) -> Tuple[float, float]:
        possible_points = [[x, y] for y in cls.params.map_spawn_y for x in cls.params.map_spawn_x if x != y]

        init = random.choice(possible_points)

        return init[0] * width, init[1] * height

    @classmethod
    def _get_flight_information(cls) -> Union[dict, None]:
        return cls.data.fetch_flight_information_for_new_aircraft(cls.op_type)

    @classmethod
    def _compute_initial_altitude(cls) -> float:
        altitude = cls.data.get_game_airport_altitude()

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
    def _compute_initial_heading(cls, x_init: float, y_init: float) -> float:
        if cls.op_type == c.departure:
            return cls.runway.get_heading()
        else:
            return cls._get_initial_angle(x_init, y_init)

    @classmethod
    def _get_initial_angle(cls, x_init: float, y_init: float) -> float:

        angle = cls.runway.get_angle_relative_to_aircraft(x_init, y_init)

        return angle + random.randint(0, cls.params.init_heading_variation)

    @classmethod
    def _find_runway(cls) -> MapRunway:
        return cls.data.get_game_active_runway()

    @classmethod
    def _find_waypoint(cls):
        return cls.data.get_game_random_waypoint()

    def _create_symbol_on_map(self):
        if self.phase != c.taxi:
            self.icon_id = self.canvas.create_rectangle(
                self.x-self.size,
                self.y-self.size,
                self.x+self.size,
                self.y+self.size,
                fill=self.fill,
                outline=self.fill
            )

            self._create_tag()

    def _create_tag(self):
        # Create tag
        self.tag_id = self.canvas.create_text(
            self.x - 23,
            self.y - 20,
            fill=self.fill,
            font="Arial 12",
            text=self._get_tag_text()
        )

        def _add_callsign_to_prompt(event, flight_no, prompt):
            prompt.delete(0, 'end')
            prompt.insert(0, f"{flight_no} ")

        # todo: improve, see suggestion
        eval_label = lambda x, y, z: (lambda p: _add_callsign_to_prompt(x, y, z))
        self.canvas.tag_bind(self.tag_id, "<Button-1>", eval_label(self, self.flight_no, self.cmd_prompt))

    def _delete_symbol_on_map(self):
        # Delete aircraft icon and tag
        self.canvas.delete(self.icon_id)
        self.canvas.delete(self.tag_id)

        # Remove all historic positions icons
        for pos_id in self.pos_history:
            self.canvas.delete(pos_id)

    def process_altitude_request(self, new_altitude: str):
        new_altitude = int(new_altitude)

        self.tgt_altitude = new_altitude

    def process_heading_request(self, new_heading: str):
        new_heading = int(new_heading)

        self.tgt_heading = new_heading

    def process_speed_request(self, new_speed: str):
        new_speed = int(new_speed)

        self.tgt_speed = new_speed

    def process_lineup_request(self, runway: str):
        # Only departures that were taxiing can accept a take-off clearance
        if self.op_type == c.departure and self.phase == c.taxi and self.runway.get_lineup() is False:
            if runway == self.runway.name:
                self.phase = c.lineup

                self.runway.lineup()

                self._create_symbol_on_map()

    def process_takeoff_request(self, runway: str):
        # Only departures that were taxiing or lining up can accept a take-off clearance
        if self.op_type == c.departure and (self.phase == c.taxi or self.phase == c.lineup):
            # The request can only happen if there is a valid clearance for speed and altitude
            if (
                self.tgt_speed >= self.params.min_speed and
                self.tgt_altitude >= self.params.min_altitude
            ):
                self.phase = c.takeoff

                self.runway.stop_lineup()

                if self.icon_id is None:
                    self._create_symbol_on_map()

            else:
                self.log_list.add_log({"aircraft": self, "type": c.dep_takeoff_invalid_spd_hdg})

    def process_ils_request(self, runway: str):
        # Only airborne aircraft can be given an ILS command
        if self.phase == c.airborne:
            self.phase = c.ils_on

    def process_landing_clearance_request(self, runway: str):
        # Only airborne aircraft can be given landing clearance
        if self.phase == c.airborne or self.phase == c.ils_on or self.phase == c.ils_intercept:
            self.phase = c.landing_clearance

    def update(self):
        # Execute state update according to flight phase
        getattr(self, f"_phase_update_{self.phase}")()

        if self._check_if_objective_was_reached():
            self.to_be_hand_over = True

    def _phase_update_taxi(self):
        """
        There are no updates to be made during taxi
        """
        pass

    def _phase_update_lineup(self):
        self._update_tag_text()

    def _phase_update_takeoff(self):
        self._update_speed(takeoff=True)

        if self.speed >= self.params.min_speed:
            self.phase = c.airborne

        # Update position
        self._update_aircraft_position()
        self._update_positions_history()

        self._move_on_map()

    def _phase_update_airborne(self):
        # Update state
        self._update_altitude()
        self._update_heading()
        self._update_speed()

        # Update position
        self._update_aircraft_position()
        self._update_positions_history()

        self._move_on_map()

    def _phase_update_ils_on(self):
        # Do all the other updates since the aircraft is still airborne
        self._phase_update_airborne()

        # Check if ILS has been intersected
        if self.runway.check_ils_interception(self.x, self.y, self.heading, self.altitude):
            self.phase = c.ils_intercept

    def _phase_update_ils_intercept(self):
        # Do all the other updates since the aircraft is still airborne
        self._phase_update_airborne()

        self._follow_runway_ils_signal()

    def _phase_update_landing_clearance(self):
        # Do all the other updates since the aircraft is still airborne
        self._phase_update_airborne()

        self._follow_runway_ils_signal()

        if self._aircraft_landing():
            self.phase = c.landing
            print(1)

    def _phase_update_landing(self):
        self.tgt_altitude = 0
        self.tgt_speed = 0

        self._update_speed()

        # Update position
        self._update_aircraft_position()
        self._update_positions_history()

        self._move_on_map()

    def _follow_runway_ils_signal(self):
        self._follow_runway_glideslope()
        self._follow_runway_localizer()

    def _aircraft_landing(self) -> bool:
        return (
            self.altitude <= self.params.min_altitude_landing and
            self.runway.get_distance_to_aircraft(self.x, self.y) <= self.params.min_distance_landing_runway * self.width
        )

    def _follow_runway_glideslope(self):
        # Get ratio of current position and maximum range of ILS
        altitude_ratio = (self.runway.get_distance_to_aircraft(self.x, self.y)) / self.runway.get_ils_localizer_range()

        # Get expected altitude altitude
        expected_altitude = altitude_ratio * self.params.ils_gs_max_altitude

        # Adjust target altitude
        self.tgt_altitude = min(self.tgt_altitude, expected_altitude)

    def _follow_runway_localizer(self):
        # Get ratio of current angle between aircraft and runway and total angular range of the ILS localizer
        angle_ratio = self.runway.get_angular_distance_to_aircraft(self.x, self.y) / self.params.ils_loc_angular_range

        # Get the necessary angle deviation from the runway's heading
        angle_deviation = self.params.ils_angle_gain * self.params.rate_change_heading * angle_ratio

        # Get correct target heading by adding the runway heading to the deviation
        final_tgt_heading = self.runway.get_heading() + angle_deviation

        # Make sure target heading is always between 1 and 360 degrees
        self.tgt_heading = final_tgt_heading if final_tgt_heading <= 360 else final_tgt_heading - 360
        self.tgt_heading = final_tgt_heading if final_tgt_heading >= 1 else final_tgt_heading + 360

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

    def _update_speed(self, takeoff: bool = False):
        if takeoff:
            # For take-off, a more gradual speed change is calculated
            self.speed += max(2, round(15 * (1 - 1 / (self.speed / 30 + 1))))
        else:
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

    def _move_on_map(self):
        self.canvas.move(self.icon_id, self.displacement_x, self.displacement_y)
        self.canvas.move(self.tag_id, self.displacement_x, self.displacement_y)

        self._update_tag_text()

    def _update_tag_text(self):
        self.canvas.itemconfigure(self.tag_id, text=self._get_tag_text(), fill=self.fill)

    def _check_if_objective_was_reached(self) -> bool:
        if self.op_type == c.departure:
            dist_to_wpt = self._get_distance(self.x, self.y, self.objective.get_x(), self.objective.get_y())
            current_alt = self.altitude

            # todo: make self.params.obj_dep_min_distance * self.width be returned by params/data_service class
            if (
                dist_to_wpt <= self.params.obj_dep_min_distance * self.width and
                current_alt >= self.params.obj_dep_min_altitude
            ):
                return True
            else:
                return False

        if self.op_type == c.arrival:
            if self.phase == c.landing and self.speed == 0:
                return True
            else:
                return False

    def remove_aircraft_from_radar(self):
        # Delete symbol
        self._delete_symbol_on_map()

        # Add points to game points
        self.data.game_data.add_to_game_points(self.points)

        # Delete from list
        self.data.game_data.remove_from_active_aircraft(self.flight_no)

    def _get_tag_text(self) -> str:
        return (
            f"{self.flight_no}\n" +
            f"{self.aircraft_type}\n" +
            f"{self.other_airport}\n" +
            f"{str(int(self.altitude))} {str(int(self.tgt_altitude))}\n" +
            f"{str(int(self.speed))} {str(int(self.tgt_speed))}\n"
        )

    def _get_speed_on_screen(self) -> float:
        return self.speed * self.data.game_data.screen_speed_conversion_factor

    def _get_distance(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return Point(x1, y1).distance((Point(x2, y2)))
