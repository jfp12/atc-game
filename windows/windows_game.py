from database.data_management_service import DataManagementService
from windows.window_base import WindowBase
from utils.windows_parameters import SingleWindowParameters
from components.section_radar import SectionRadar
from components.section_sidebar import SectionSidebar


class WindowGame(WindowBase):
    def __init__(self, data_service: DataManagementService, win_parameters: SingleWindowParameters):
        super().__init__(data_service, win_parameters)

        self.r_width = None
        self.r_height = None

        self._open_canvas()
        self._set_radar_dimensions()
        self._create_window_elements()

        self.window.mainloop()

    def _create_window_elements(self):
        self._create_sections(
            [
                {
                    "name": SectionRadar.__name__, "bg": self.params.background_colour, "width": self.r_width,
                    "height": self.r_height, "x": 0, "y": 0
                },
                {
                    "name": SectionSidebar.__name__, "bg": self.params.sidebar_colour,
                    "width": (self.w_width - self.r_width), "height": self.r_height, "x": self.r_width, "y": 0
                }
            ]
        )

    def _set_radar_dimensions(self):
        self.r_width = int(self.w_width * self.params.radar_width)
        self.r_height = int(self.w_height * self.params.radar_height)
