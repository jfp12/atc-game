from components.section_base import SectionBase
from data_management.game_data_service import GameDataService
from components.saves_list import SavesList


class SectionInGameSave(SectionBase):
    def __init__(self, window, kwargs, data: GameDataService, window_name: str):
        super().__init__(window, kwargs, data, window_name)

        self.saves_list = None

        self._create_elements()

    def _create_elements(self):
        self._create_saves_list()

    def _create_saves_list(self):
        self.saves_list = SavesList(
            self.data,
            self.window_name,
            self.window,
            self.width,
            self.height,
            self.canvas
        )
