import os
from pathlib import Path

import tkinter as tk

from data_management.game_data_service import GameDataService
from base.base import Base


class SavesList(Base):
    def __init__(
            self,
            data: GameDataService,
            window_name,
            window,
            width: int,
            height: int,
            canvas
    ):

        super().__init__(data, window_name, window, width, height, canvas)

        self.x = self.p().saves_list_x0 * width
        self.y = self.p().saves_list_y0 * height
        self.bg = self.p().saves_list_colour
        self.scrollable_frame = None

        self._create()
        self._add_saved_games()

    def _create(self):
        container = tk.Frame(
            self.window,
            bg=self.bg,
            width=self.p().saves_list_width * self.width,
            height=self.p().saves_list_height * self.height
        )
        container.place(x=self.x, y=self.y)

        canvas = tk.Canvas(
            container,
            bg=self.bg,
            width=self.p().saves_list_width * self.width,
            height=self.p().saves_list_height * self.height,
            bd=0,
            highlightbackground=self.bg
        )

        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        self.scrollable_frame = tk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="none", expand=False)

        scrollbar.pack(side="right", fill="y")

    def _add_saved_games(self):

        saves_path = Path(__file__).parents[1] / self.data.game_data.saves_location

        if not saves_path.is_dir():
            self._close_window()
            raise NotADirectoryError(f"The saved files folder could not be found. Window will be closed")

        eval_label = lambda obj, _savename: (lambda p: self._save_game(obj, _savename))

        for save in os.listdir(self.data.game_data.saves_location):

            save_name = Path(save).stem

            _save = tk.Label(
                self.scrollable_frame,
                anchor="w",
                font=self.p().main_font,
                text=save_name,
                bg=self.p().saves_list_colour,
                fg=self.p().saves_list_font_colour,
                borderwidth=0,
                width=int(self.width),
                height=1
            )

            _save.pack()
            _save.bind("<Double-Button-1>", eval_label(self, _save))

    def _save_game(self, a, b):
        print(self.height, a)
