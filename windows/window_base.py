import tkinter as tk

from data_management.game_data_management_service import GameDataManagementService
import components
from base.base import Base


class WindowBase(Base):
    def __init__(self, data: GameDataManagementService, window_name: str):
        super().__init__(self.window, data, window_name)

        self.s_width = None
        self.s_height = None
        self.x_pos = None
        self.y_pos = None
        self.background = None
        self.window = None
        self.canvas = None
        self.title = None

        self.sections = {}

        self._open_and_setup_window()

    def _open_and_setup_window(self):
        self._open_window()
        self._setup_window()

    def _open_window(self):
        self.window = tk.Tk()

    def _setup_window(self):
        self._set_screen_dimensions()

        # Choose the correct dimensions type: either full screen or defined dimensions
        if isinstance(self.p().width, str):
            self.window.attributes('-fullscreen', True)
        else:
            self._set_width(int(self.s_width * self.p().width))
            self._set_height(int(self.s_height * self.p().height))
            self.x_pos = int((1 - self.p().width) / 2 * self.s_width)
            self.y_pos = int((1 - self.p().height) / 2 * self.s_height)
            self.window.geometry(f"{self.width}x{self.height}+{self.x_pos}+{self.y_pos}")

        self.background = self.p().background_colour
        self.window.configure(bg=self.background)
        self.title = self.p().title
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
            self.sections[section["name"]] = section_class(self.window, self.p(), section, self.data)
