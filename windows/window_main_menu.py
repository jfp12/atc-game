import pygame

from database.data_management_service import DataManagementService
from windows.window_base import WindowBase


class WindowMainMenu(WindowBase):
    def __init__(self, data_service: DataManagementService):
        super().__init__(data_service)

        self._set_window_size(self.parameters.width_main_menu, self.parameters.height_main_menu)
        self._open_window()

        pygame.display.flip()

