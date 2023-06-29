from data_management.game_data_service import GameDataService


class Map:
    canvas = None
    width = None
    height = None
    data_service = None
    params = None

    def __init__(self):
        pass

    @classmethod
    def draw(cls, canvas, width: float, height: float, data_service: GameDataService, params):
        cls.canvas = canvas
        cls.width = width
        cls.height = height
        cls.data_service = data_service
        cls.params = params

        cls._draw_waypoints()
        cls._draw_runways()

        return cls()

    @classmethod
    def _draw_waypoints(cls):

        for wpt_name, wpt in cls.data_service.get_game_waypoints().items():
            wpt.define_window_parameters(cls.canvas, cls.width, cls.height, cls.params, cls.params.wpt_colour)
            wpt.define_centre()

            wpt.draw()

    @classmethod
    def _draw_runways(cls):

        for rwy_name, rwy in cls.data_service.get_game_runways().items():
            rwy.define_window_parameters(cls.canvas, cls.width, cls.height, cls.params, cls.params.rwy_colour)
            rwy.define_ends()

            rwy.draw()
