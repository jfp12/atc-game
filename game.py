import pygame

from database.data_management_service import DataManagementService
from windows.window_main_menu import WindowMainMenu


# Variables, to remove
DB_URL = "sqlite:///./atc_game.db"
AIRPORT = "LIS"


def game():
    data_service = DataManagementService(db_url=DB_URL)
    data_service.load_base_data()

    pygame.init()

    WindowMainMenu(data_service)

    while True:
        pass

    data_service.close_db_connection()


if __name__ == "__main__":
    game()
