from components.section_base import SectionBase
from utils.windows_parameters import SingleWindowParameters
from database.data_management_service import DataManagementService


class SectionRadar(SectionBase):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: DataManagementService):
        super().__init__(window, params, kwargs, data_service)
