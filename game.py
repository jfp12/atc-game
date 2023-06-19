from data_management.game_data_management_service import GameDataManagementService
from windows.window_main_menu import WindowMainMenu
from windows.windows_game import WindowGame

# Variables, to remove
DB_URL = "sqlite:///./atc_game.db"
AIRPORT = "LIS"


def game():

    data = GameDataManagementService(db_url=DB_URL)
    data.load_base_data()

    while data.game_data.opened_window != data.window_codes.EXIT:

        if data.game_data.opened_window == data.window_codes.MAIN_MENU:
            WindowMainMenu(data)
        if data.game_data.opened_window == data.window_codes.GAME:
            WindowGame(data)

    data.close_db_connection()


if __name__ == "__main__":
    game()
