from base.base import Base
from utils.windows_parameters import SingleWindowParameters
from data_management.game_data_management_service import GameDataManagementService


class PointsCounter(Base):
    def __init__(
            self, window, canvas, width, height, params: SingleWindowParameters, data_service: GameDataManagementService
    ):
        super().__init__(window, width, height, params, data_service, canvas)

        self.x0 = self.width * self.params.point_counter_x0
        self.y0 = self.height * self.params.point_counter_y0

        self.points_id = None

        self._create()

    def _create(self):
        self.points_id = self.canvas.create_text(
            self.x0,
            self.y0,
            fill=self.params.point_counter_colour,
            font=f"{self.params.main_font} {self.params.point_counter_font_size}",
            text=self._get_text(),
            anchor="e"
        )

    def update_text(self):
        self.canvas.itemconfigure(self.points_id, text=self._get_text())

    def _get_text(self) -> str:
        return self.params.point_counter_text.format(points=self.data_service.game_data.game_points)
