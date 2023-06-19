from windows.window_base import WindowBase
from data_management.game_data_management_service import GameDataManagementService


class WindowInGameSave(WindowBase):
    def __init__(self, data: GameDataManagementService):
        super().__init__(data)
