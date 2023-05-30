from data_management.input_data_management_service import InputDataManagementService

INPUT_URL = "file://./data/"
DB_URL = "sqlite:///./atc_game.db"

if __name__ == "__main__":
    data_service = InputDataManagementService(INPUT_URL, DB_URL)

    data_service.load_file(filename="airports.csv", tablename="airports")
    data_service.load_file(filename="runways.csv", tablename="runways")
    data_service.load_file(filename="waypoints.csv", tablename="waypoints")

    data_service.close_db_connection()
