import math

import pandas as pd

from components.map.map_component_base import MapComponentBase


class MapRunway(MapComponentBase):
    def __init__(self, runway: pd.Series):
        super().__init__()

        self.name = runway["name"].zfill(2)
        self.length = runway["length"]
        self.heading = runway["heading"]
        self.x_init = runway["x_init"]
        self.y_init = runway["y_init"]
        self.x_final = runway["x_final"]
        self.y_final = runway["y_final"]

        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None

        self.aircraft_lineup = False

    def check_ils_interception(self, x: float, y: float):
        self._check_localizer_interception(x, y)

    def _check_localizer_interception(self, x: float, y: float):

        # Get angle between runway start and aircraft
        angle = self.get_angle_relative_to_aircraft(x, y)

        # Get angle different between runway heading and angle between aircraft and runway
        angle_difference = min(abs(angle - self.heading), 360 - abs(angle - self.heading))


    def get_angle_relative_to_aircraft(self, x: float, y: float) -> float:
        # Get arc-tangent values
        xx = (self.get_x_init() - x)
        yy = (self.get_y_init() - y)

        # Get angle between aircraft's initial position and runway start point
        angle = math.atan2(xx, -yy) * 180 / math.pi
        if angle < 0:
            angle += 360

        return angle

    def _create_ils_localizer_area(self):
        pass

    def define_ends(self):
        self.x0 = self.x_init * self.width
        self.y0 = self.y_init * self.height
        self.x1 = self.x_final * self.width
        self.y1 = self.y_final * self.height

    def draw(self):
        self._draw_line(self.x0, self.y0, self.x1, self.y1)

        self._add_name()

    def _add_name(self):
        self.canvas.create_text(
            self.x0,
            self._compute_text_y_position_based_on_heading(),
            fill=self.colour,
            font="Arial 10",
            text=self.name
        )

    def _compute_text_y_position_based_on_heading(self) -> float:
        if self.heading <= 90 or self.heading >= 270:
            return self.y0 + 10
        else:
            return self.y0 - 10

    def get_name(self) -> str:
        return self.name

    def get_x_init(self) -> float:
        return self.x_init * self.width

    def get_y_init(self) -> float:
        return self.y_init * self.height

    def get_heading(self) -> float:
        return self.heading

    def get_lineup(self):
        return self.aircraft_lineup

    def lineup(self):
        self.aircraft_lineup = True

    def stop_lineup(self):
        self.aircraft_lineup = False
