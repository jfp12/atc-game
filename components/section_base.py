import tkinter as tk

from data_management.game_data_management_service import GameDataManagementService
from base.base import Base


class SectionBase(Base):
    def __init__(self, window, kwargs, data: GameDataManagementService):
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
        super().__init__(self.window, self.width, self.height, self.params, data, self.canvas)

    def _create(self):
        self.section = tk.Frame(self.window, bg=self.bg, width=self.width, height=self.height)
        self.section.place(x=self.x0, y=self.y0)

        self.canvas = tk.Canvas(
            self.section, bg=self.bg, width=self.width, height=self.height, bd=0, highlightbackground=self.bg
        )
        self.canvas.pack()
