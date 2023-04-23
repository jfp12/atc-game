from tkinter import Button, Tk

BUTTON_FONT = "Bahnschrift"

class ATCButtonCreate:
    window: Tk = None
    text: str = None
    command = None


class ATCButton:
    def __init__(self, kwargs):

        kwargs["font"] = BUTTON_FONT

        self.button = Button(**kwargs)
        self.button.pack(side="top")
