from database.data_management_service import DataManagementService
from windows.window_main_menu import WindowMainMenu
from windows.windows_game import WindowGame
from utils.window_codes import WindowCodes
from utils.windows_parameters import WindowsParameters

# Variables, to remove
DB_URL = "sqlite:///./atc_game.db"
AIRPORT = "LIS"


def game():
    win_parameters = WindowsParameters()

    data_service = DataManagementService(db_url=DB_URL)
    data_service.load_base_data()

    if data_service.game_data.opened_window == WindowCodes.MAIN_MENU:
        WindowMainMenu(data_service, win_parameters.main)
    if data_service.game_data.opened_window == WindowCodes.GAME:
        WindowGame(data_service, win_parameters.game)

    data_service.close_db_connection()


if __name__ == "__main__":
    game()
