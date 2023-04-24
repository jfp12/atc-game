from database.data_management_service import DataManagementService
from windows.window_base import WindowBase
from utils.windows_parameters import SingleWindowParameters


class WindowGame(WindowBase):
    def __init__(self, data_service: DataManagementService, win_parameters: SingleWindowParameters):
        super().__init__(data_service, win_parameters)
