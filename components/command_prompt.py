import tkinter as tk

from utils.windows_parameters import SingleWindowParameters
from utils.colours import Colours


class CommandPrompt:
    def __init__(self, canvas, width: float, height: float, params: SingleWindowParameters):
        self.prompt = None

        self._create(canvas, width, height, params)

    def _create(self, canvas, width: float, height: float, params: SingleWindowParameters):
        canvas.create_rectangle(
            params.cmd_prompt_x0 * width,
            params.cmd_prompt_y0 * height,
            params.cmd_prompt_x1 * width,
            params.cmd_prompt_y1 * height,
            fill=Colours.BLACK
        )

        canvas.create_text(
            params.cmd_prompt_title_x0 * width,
            params.cmd_prompt_title_y0 * height,
            font=(params.main_font, int(params.cmd_prompt_title_font_size * width)),
            text=params.cmd_prompt_title,
            fill=params.cmd_prompt_title_font_colour
        )

        self.prompt = tk.Entry(
            canvas,
            font=(params.main_font, int(params.cmd_prompt_input_font_size * width)),
            width=params.cmd_prompt_input_width
        )
        self.prompt.place(
            x=params.cmd_prompt_input_x0 * width,
            y=params.cmd_prompt_input_y0 * height
        )
