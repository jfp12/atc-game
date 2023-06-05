import math

from utils.windows_parameters import SingleWindowParameters


class MapWaypoint:
    canvas = None
    width = None
    height = None
    params = None

    def __init__(self, waypoint: dict):
        self.name = waypoint["name"]
        self.x =  waypoint["x"]
        self.y = waypoint["y"]

        self.x0 = None
        self.y0 = None

    def draw_base(self):
        self._draw_circle(self.x0, self.y0, 0.05 * self.params.wpt_size * self.width, fill=True)

        self._add_name()

    def define_window_parameters(self, canvas, width: float, height: float, params: SingleWindowParameters):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.params = params

    def define_centre(self):
        self.x0 = self.x * self.width
        self.y0 = self.y * self.height

    def _add_name(self):
        self.canvas.create_text(
            self.x0,
            self.y0 + 20,
            fill=self.params.wpt_colour,
            font="Arial 10",
            text=self.name
        )

    def _draw_circle(self, x: float, y: float, radius: float, fill: bool = False):
        self.canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            outline=self.params.wpt_colour,
            fill=self.params.wpt_colour if fill else ""
        )

    def _draw_rectangle(self, x: float, y: float, half_width: float, half_height: float):
        self.canvas.create_rectangle(
            x - half_width,
            y - half_height,
            x + half_width,
            y + half_height,
            outline=self.params.wpt_colour
        )

    def _draw_line(self, xs: float, ys: float, xf: float, yf: float):
        self.canvas.create_line(
            xs,
            ys,
            xf,
            yf,
            fill=self.params.wpt_colour
        )

    def _draw_hexagon(self, x: float, y: float, half_width: float):
        sides = 6
        side_length = 2 * (half_width // 2) * math.sin(math.pi / sides)
        apothem = side_length / (2 * math.tan(math.pi / sides))
        ind_angle = 2 * math.pi / sides

        previous_x = x - side_length // 2
        previous_y = y - apothem

        for pdx in range(sides):
            angle = ind_angle * pdx
            x_new = previous_x + math.cos(angle) * side_length
            y_new = previous_y + math.sin(angle) * side_length

            self._draw_line(previous_x, previous_y, x_new, y_new)

            previous_x = x_new
            previous_y = y_new


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

        half_height = 0.3 * self.params.wpt_size * self.width
        half_width = 0.4 * self.params.wpt_size * self.width
        bbox = 0.8 * self.params.wpt_size * self.width

        self._draw_rectangle(self.x0, self.y0, half_width, half_height)
        self._draw_hexagon(self.x0, self.y0, bbox)


class MapVortac(MapWaypoint):

    def draw(self):
        self.draw_base()

        bbox = 0.8 * self.params.wpt_size * self.width

        self._draw_hexagon(self.x0, self.y0, bbox)


class MapTacan(MapWaypoint):

    def draw(self):
        self.draw_base()

        bbox = 0.8 * self.params.wpt_size * self.width

        self._draw_hexagon(self.x0, self.y0, bbox)
