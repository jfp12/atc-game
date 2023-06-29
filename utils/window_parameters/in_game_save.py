from utils.window_parameters.common import WindowParametersCommon
from utils.colours import Colours


class InGameSaveWindowParametersBase(WindowParametersCommon):
    pass


class InGameSaveWindowParameters(InGameSaveWindowParametersBase):
    def __init__(self):
        self.title = "Save Game"
        self.width = 0.4
        self.height = 0.6
        self.button_colour = Colours.LIGHT_GREY
        self.main_font = "Bahnschrift 25"
        self.button_font_colour = Colours.BLACK

        self.body_x = 0
        self.body_y = 0
        self.body_width = 1
        self.body_height = 0.85
        self.body_background_colour = Colours.LIGHT_GREY

        self.footer_x = 0
        self.footer_y = 0.85
        self.footer_width = 1
        self.footer_height = 0.15
        self.footer_background_colour = Colours.DARK_GREY
        self.footer_button_width = 0.3
        self.footer_button_height = 0.5
        self.footer_button_save_x = 0.1
        self.footer_button_save_y = 0.25
        self.footer_button_save_text = "Save"
        self.footer_button_cancel_x = 0.6
        self.footer_button_cancel_y = 0.25
        self.footer_button_cancel_text = "Cancel"

        self.saves_list_x0 = 0.2
        self.saves_list_y0 = 0.2
        self.saves_list_width = 0.55
        self.saves_list_height = 0.7
        self.saves_list_colour = Colours.DARK_GREY
        self.saves_list_font_colour = Colours.BLACK
