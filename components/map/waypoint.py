from components.map.map_component_base import MapComponentBase


class MapWaypoint(MapComponentBase):

    def __init__(self, waypoint: dict):
        super().__init__()

        self.name = waypoint["name"]
        self.x =  waypoint["x"]
        self.y = waypoint["y"]

        self.x0 = None
        self.y0 = None

    def draw_base(self):
        self._draw_circle(self.x0, self.y0, 0.05 * self.params.wpt_size * self.width, fill=True)

        self._add_name()

    def define_centre(self):
        self.x0 = self.x * self.width
        self.y0 = self.y * self.height

    def _add_name(self):
        self.canvas.create_text(
            self.x0,
            self.y0 + 20,
            fill=self.colour,
            font="Arial 10",
            text=self.name
        )


class MapNdb(MapWaypoint):

    def draw(self):
        self.draw_base()

        radius = 0.5 * self.params.wpt_size * self.width

        self._draw_circle(self.x0, self.y0, radius)
        self._draw_circle(self.x0, self.y0, 0.7 * radius)
        self._draw_circle(self.x0, self.y0, 0.4 * radius)
        self._draw_circle(self.x0, self.y0, 0.1 * radius)


class MapVorDme(MapWaypoint):

    def draw(self):
        self.draw_base()

        half_height = 0.4 * self.params.wpt_size * self.width
        half_width = 0.5 * self.params.wpt_size * self.width

        self._draw_rectangle(self.x0, self.y0, half_width, half_height)
        self._draw_hexagon(self.x0, self.y0, half_width, half_height)


class MapVortac(MapWaypoint):

    def draw(self):
        self.draw_base()

        half_height = 0.4 * self.params.wpt_size * self.width
        half_width = 0.5 * self.params.wpt_size * self.width

        self._draw_hexagon_uneven_sides(self.x0, self.y0, half_width, half_height)


class MapTacan(MapWaypoint):

    def draw(self):
        self.draw_base()

        half_height = 0.4 * self.params.wpt_size * self.width
        half_width = 0.5 * self.params.wpt_size * self.width

        self._draw_hexagon_uneven_sides(self.x0, self.y0, half_width, half_height)
