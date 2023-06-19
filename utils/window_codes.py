class WindowCodes:

    def __init__(self):
        from windows import (
            WindowMainMenu,
            WindowGame,
            WindowInGameSave
        )

        self.EXIT = "exit"
        self.MAIN_MENU = WindowMainMenu.__name__
        self.GAME = WindowGame.__name__
        self.IN_GAME_SAVE = WindowInGameSave.__name__
