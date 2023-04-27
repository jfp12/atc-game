import tkinter as tk

from database.data_management_service import DataManagementService
from utils.windows_parameters import SingleWindowParameters
from base.base import Base


class SectionBase(Base):
    def __init__(self, window, params: SingleWindowParameters, kwargs, data_service: DataManagementService):
        self.params = params
        self.window = window
        self.name = kwargs["name"]
        self.bg = kwargs["bg"]
        self.width = kwargs["width"]
        self.height = kwargs["height"]
        self.x0 = kwargs["x"]
        self.y0 = kwargs["y"]

        self.section = None
        self.canvas = None
        self._create()
        super().__init__(self.window, self.width, self.height, self.params, data_service)

    def _create(self):
        self.section = tk.Frame(self.window, bg=self.bg, width=self.width, height=self.height)
        self.section.place(x=self.x0, y=self.y0)

        self.canvas = tk.Canvas(
            self.section, bg=self.bg, width=self.width, height=self.height, bd=0, highlightbackground=self.bg
        )
