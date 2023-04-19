import pygame

from database.database_connection_service import DatabaseConnectionService

def game():
    db_service = DatabaseConnectionService("sqlite:///./atc_game.db")

    db_service.save_all_data()

    pygame.init()


if __name__ == "__main__":
    game()
