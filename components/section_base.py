import tkinter as tk

from data_management.game_data_service import GameDataService
from base.base import Base


class SectionBase(Base):
    def __init__(self, window, kwargs, data: GameDataService, window_name: str):
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

        super().__init__(data, window_name, self.window, self.width, self.height, self.canvas)

    def _create(self):
        self.section = tk.Frame(self.window, bg=self.bg, width=self.width, height=self.height)
        self.section.place(x=self.x0, y=self.y0)

        self.canvas = tk.Canvas(
            self.section, bg=self.bg, width=self.width, height=self.height, bd=0, highlightbackground=self.bg
        )
        self.canvas.pack()
