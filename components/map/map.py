from data_management.game_data_management_service import GameDataManagementService
from utils.windows_parameters import SingleWindowParameters


class Map:
    canvas = None
    width = None
    height = None
    data_service = None
    params = None

    def __init__(self):
        pass

    @classmethod
    def draw(cls, canvas, width: float, height: float, data_service: GameDataManagementService, params: SingleWindowParameters):
        cls.canvas = canvas
        cls.width = width
        cls.height = height
        cls.data_service = data_service
        cls.params = params

        cls._draw_waypoints()

        return cls()

    @classmethod
    def _draw_waypoints(cls):

        for wpt_name, wpt in cls.data_service.get_game_waypoints().items():
            wpt.define_window_parameters(cls.canvas, cls.width, cls.height, cls.params)
            wpt.define_centre()

            wpt.draw()
