import tkinter as tk

from database.data_management_service import DataManagementService
import components
from utils.windows_parameters import SingleWindowParameters
from base.base import Base


class WindowBase(Base):
    def __init__(self, data_service: DataManagementService, params: SingleWindowParameters):
        self.params = params
        self.s_width = None
        self.s_height = None
        self.w_width = None
        self.w_height = None
        self.x_pos = None
        self.y_pos = None
        self.background = None
        self.window = None
        self.canvas = None
        self.title = None

        self.sections = {}

        self._open_and_setup_window()
        super().__init__(self.window, self.w_width, self.w_height, self.params, data_service)

    def _open_and_setup_window(self):
        self._open_window()
        self._setup_window()

    def _open_window(self):
        self.window = tk.Tk()
        self._set_screen_dimensions()

    def _setup_window(self):

        # Choose the correct dimensions type: either full screen or defined dimensions
        if isinstance(self.params.width, str):
            self.window.attributes('-fullscreen', True)
        else:
            self.w_width = int(self.s_width * self.params.width)
            self.w_height = int(self.s_height * self.params.height)
            self.x_pos = int((1 - self.params.width) / 2 * self.s_width)
            self.y_pos = int((1 - self.params.height) / 2 * self.s_height)
            self.window.geometry(f"{self.w_width}x{self.w_height}+{self.x_pos}+{self.y_pos}")

        self.background = self.params.background_colour
        self.window.configure(bg=self.background)
        self.title = self.params.title
        self.window.title(self.title)

    def _open_canvas(self):
        self.canvas = tk.Canvas(self.window, bd=0, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

    def _set_screen_dimensions(self):
        self.s_width = self.window.winfo_screenwidth()
        self.s_height = self.window.winfo_screenheight()

    def _create_sections(self, sections: list):
        for section in sections:
            section_class = getattr(components, section["name"])
            self.sections[section["name"]] = section_class(self.window, self.params, section, self.data_service)
