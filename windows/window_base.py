import pygame

from database.data_management_service import DataManagementService


class WindowBase:
    def __init__(self, data_service: DataManagementService):
        self.parameters = data_service.get_parameters()

        self.w_width = None
        self.w_height = None
        self.window = None

    def _set_window_size(self, width: float, height: float):
        self.w_width = self.parameters.width_screen * width
        self.w_height = self.parameters.height_screen * height

    def _open_window(self):
        self.window = pygame.display.set_mode((self.w_width, self.w_height))
