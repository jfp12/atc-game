class MapComponentBase:
    def __init__(self):
        self.canvas = None
        self.width = None
        self.height = None
        self.params = None
        self.colour = None

    def define_window_parameters(
        self, canvas, width: float, height: float, params, colour: str
    ):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.params = params
        self.colour = colour

    def _draw_line(self, xs: float, ys: float, xf: float, yf: float):
        self.canvas.create_line(
            xs,
            ys,
            xf,
            yf,
            fill=self.colour
        )

    def _draw_circle(self, x: float, y: float, radius: float, fill: bool = False):
        self.canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            outline=self.colour,
            fill=self.colour if fill else ""
        )

    def _draw_rectangle(self, x: float, y: float, half_width: float, half_height: float):
        self.canvas.create_rectangle(
            x - half_width,
            y - half_height,
            x + half_width,
            y + half_height,
            outline=self.colour
        )

    def _draw_hexagon(self, x: float, y: float, half_width: float, half_height: float):
        self._draw_hexagon_even_sides(x, y, half_width, half_height)
        self._draw_hexagon_uneven_sides(x, y, half_width, half_height)

    def _draw_hexagon_even_sides(self, x: float, y: float, half_width: float, half_height: float):
        self._draw_line(x - half_width, y, x - 0.4 * half_width, y - half_height)
        self._draw_line(x + 0.4 * half_width, y - half_height, x + half_width, y)
        self._draw_line(x + 0.4 * half_width, y + half_height, x - 0.4 * half_width, y + half_height)

    def _draw_hexagon_uneven_sides(self, x: float, y: float, half_width: float, half_height: float):
        self._draw_line(x - 0.4 * half_width, y - half_height, x + 0.4 * half_width, y - half_height)
        self._draw_line(x + half_width, y, x + 0.4 * half_width, y + half_height)
        self._draw_line(x - 0.4 * half_width, y + half_height, x - half_width, y)
