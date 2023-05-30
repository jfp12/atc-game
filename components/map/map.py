class Map:
    canvas = None
    width = None
    height = None

    def __init__(self, canvas, width: float, height: float):
        self.canvas = canvas
        self.width = width
        self.height = height

    @classmethod
    def _draw(cls, canvas, width: float, height: float):
        cls.canvas = canvas
        cls.width = width
        cls.height = height

        cls._draw_waypoints()

        return cls(canvas, width, height)

    @classmethod
    def _draw_waypoints(cls):
        pass
