import tkinter as tk
from typing import Union

from aircraft.aircraft import Aircraft
from utils.windows_parameters import SingleWindowParameters
from utils.colours import Colours
from data_management.game_data_management_service import GameDataManagementService


class CommandPrompt:

    def __init__(self, canvas, width: float, height: float, params: SingleWindowParameters, data_service: GameDataManagementService):
        self.params = params
        self.data_service = data_service

        self.prompt = None

        self._create(canvas, width, height)

    def _create(self, canvas, width: float, height: float,):
        canvas.create_rectangle(
            self.params.cmd_prompt_x0 * width,
            self.params.cmd_prompt_y0 * height,
            self.params.cmd_prompt_x1 * width,
            self.params.cmd_prompt_y1 * height,
            fill=Colours.BLACK
        )

        canvas.create_text(
            self.params.cmd_prompt_title_x0 * width,
            self.params.cmd_prompt_title_y0 * height,
            font=(self.params.main_font, int(self.params.cmd_prompt_title_font_size * width)),
            text=self.params.cmd_prompt_title,
            fill=self.params.cmd_prompt_title_font_colour
        )

        self.prompt = tk.Entry(
            canvas,
            font=(self.params.main_font, int(self.params.cmd_prompt_input_font_size * width)),
            width=self.params.cmd_prompt_input_width
        )
        self.prompt.place(
            x=self.params.cmd_prompt_input_x0 * width,
            y=self.params.cmd_prompt_input_y0 * height
        )
        self.prompt.bind("<Return>", self.process_input)

    def process_input(self, event):
        # Get command
        command = self.prompt.get()

        # Clear the prompt
        self.prompt.delete(0, 'end')

        # Try to get the 3 elements of the command. Stop processing if command could not be correctly parsed
        try:
            flight_no, action, value = [elements for elements in command.split(" ")]
        except ValueError:
            return

        for aircraft in self.data_service.game_data.active_aircraft:
            _action = self._convert_action_name(action)

            # If action is not valid, stop processing
            if not _action:
                return

            # Check if value is valid for the requested action, and, if that is the case, perform request
            if getattr(self, f"_check_{_action}_validity")(value):
                getattr(self, f"_process_{_action}_request")(aircraft, value)

    def _convert_action_name(self, action: str) -> Union[str, None]:
        for action_name, action_possibilities in self.params.actions.items():
            if action in action_possibilities:
                return action_name

        return None

    def _check_altitude_validity(self, altitude: str) -> bool:
        altitude = int(altitude)

        if altitude < self.params.min_altitude or altitude > self.params.max_altitude:
            return False
        return True

    def _process_altitude_request(self, aircraft: Aircraft, altitude: str):
        aircraft.tgt_altitude = int(altitude)