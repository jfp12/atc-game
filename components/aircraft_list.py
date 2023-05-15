import tkinter as tk
from typing import Tuple

from utils.windows_parameters import SingleWindowParameters
from database.data_management_service import DataManagementService
from base import constants as c
from base.base import Base
from aircraft.aircraft import Aircraft


# todo: make this class a parent of section sidebar?
class AircraftList(Base):
    def __init__(
            self,
            data_service: DataManagementService,
            width: int,
            height: int,
            window,
            canvas,
            bg: str,
            params: SingleWindowParameters
    ):
        super().__init__(
            window,
            params.aircraft_list_width * width,
            params.aircraft_list_height * height,
            params,
            data_service,
            canvas
        )

        self.x = self.params.aircraft_list_x0 * width
        self.y = self.params.aircraft_list_y0 * height
        self.bg = bg
        self.scrollable_frame = None
        self.length = None

        self._create()
        self._add_title()
        self._set_label_field_length()

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

    def _add_title(self):
        self.canvas.create_text(
            self.params.aircraft_list_title_x0 * self.width,
            self.params.aircraft_list_title_y0 * self.height,
            font=("Bahnschrift", 25),
            fill='black',
            text=self.params.aircraft_list_title
        )

    # todo: add methods to add single aircraft and remove single aircraft
    def add_aircraft_to_list(self):
        # Clear Frame
        label = []
        for arc in self.scrollable_frame.winfo_children():
            arc.destroy()

        # eval_label = lambda x, y, z: (lambda p: self.add_callsign_to_prompt(x, y, z))

        for aircraft in self.data_service.game_data.active_aircraft:
            # ils_state = ""
            # if aircraft.ils_status == "on":
            #     ils_state = "ILS " + aircraft.ils_runway
            # if aircraft.ils_status == "intersect":
            #     ils_state = "ILS " + aircraft.ils_runway + " INT"

            # l = int(self.width / 170)

            label.append(
                tk.Label(
                    self.scrollable_frame,
                    justify="left",
                    font=f"{self.params.main_font} {self._calculate_font_size()}",
                    text=self._get_label_text(aircraft),
                    bg=self._get_label_colour(aircraft),
                    foreground=self.params.aircraft_list_font_colour,
                    borderwidth=2,
                    relief="solid",
                    width=int(0.125 * self.width),
                    height=3,
                )
            )
            label[-1].pack()
            # label[-1].bind("<Button-1>", eval_label(self, aircraft.flight_no, cmd_prompt))

    def _get_label_text(self, aircraft: Aircraft) -> str:
        # txt = aircraft.flight_no.ljust(l) + aircraft.aircraft.ljust(l) + obj + '\n' + \
        #       str(format(aircraft.alt, "05")).ljust(l) + str(format(aircraft.speed, "03")).ljust(
        #     l) + aircraft.objective + '\n' + \
        #       str(format(aircraft.tgt_alt, "05")).ljust(l) + str(format(aircraft.tgt_speed, "03")).ljust(
        #     l) + ils_state

        if aircraft.op_type == c.departure:
            op_type = self.params.aircraft_list_departure_text
        else:
            op_type = self.params.aircraft_list_arrival_text

        return (
            f"{'TS123'.ljust(self.length)} {'A320'.ljust(self.length)} {op_type} {aircraft.airport}\n" +
            f"{self._format_alt(aircraft.alt)} {self._format_spd(aircraft.speed)} OBJ\n" +
            f"{self._format_alt(aircraft.tgt_alt)} {self._format_spd(aircraft.tgt_speed)} ILS"
        )

    def _format_alt(self, value: float, ) -> str:
        return str(format(int(value), '05')).ljust(self.length)

    def _format_spd(self, value: float) -> str:
        return str(format(int(value), '03')).ljust(self.length)

    def _set_label_field_length(self):
        self.length = int(0.08 * self.width)

    def _get_label_colour(self, aircraft: Aircraft) -> str:
        if aircraft.op_type == c.departure:
            return self.params.aircraft_list_departure_colour
        else:
            return self.params.aircraft_list_arrival_colour
