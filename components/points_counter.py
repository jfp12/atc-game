from base.base import Base
from data_management.game_data_management_service import GameDataManagementService


class PointsCounter(Base):
    def __init__(
            self, data: GameDataManagementService, window_name, window, width, height, canvas
    ):
        super().__init__(data, window_name, window, width, height, canvas)

        self.x0 = self.width * self.p().point_counter_x0
        self.y0 = self.height * self.p().point_counter_y0

        self.points_id = None

        self._create()

    def _create(self):
        self.points_id = self.canvas.create_text(
            self.x0,
            self.y0,
            fill=self.p().point_counter_colour,
            font=f"{self.p().main_font} {self.p().point_counter_font_size}",
            text=self._get_text(),
            anchor="e"
        )

    def update_text(self):
        self.canvas.itemconfigure(self.points_id, text=self._get_text())

    def _get_text(self) -> str:
        return self.p().point_counter_text.format(points=self.data.game_data.game_points)
