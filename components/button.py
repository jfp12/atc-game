from tkmacosx import Button


class ButtonATC:
    def __init__(self, kwargs):

        x = kwargs.pop("x")
        y = kwargs.pop("y")

        self.button = Button(**kwargs)
        self.button.place(x=x, y=y)
