import tkinter as tk

from utils.windows_parameters import SingleWindowParameters


class AircraftList:
    def __init__(self, width: int, height: int, window, canvas, bg: str, params: SingleWindowParameters):
        self.params = params
        self.width = self.params.aircraft_list_width * width
        self.height = self.params.aircraft_list_height * height
        self.x = self.params.aircraft_list_x0 * width
        self.y = self.params.aircraft_list_y0 * height
        self.bg = bg

        self.window = window
        self.canvas = canvas
        self.scrollable_frame = None

        self._create()
        self._add_text()

    def _create(self):
        container = tk.Frame(self.window, bg=self.bg, width=self.width, height=self.height)
        container.place(x=self.x, y=self.y)

        canvas = tk.Canvas(
            container, bg=self.bg, width=self.width, height=self.height, bd=0, highlightbackground=self.bg
        )

        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        self.scrollable_frame = tk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="none", expand=False)

        scrollbar.pack(side="right", fill="y")

    def _add_text(self):
        pass
        # self.canvas.create_text((0.5 + 0.5 * def_width) * self.screen_width, 0.03 * self.screen_height,
        #                         font="Bahnschrift " + str(size), text="Active Flights List")
