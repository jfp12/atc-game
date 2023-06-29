from typing import Tuple

from datetime import datetime

from base.base import Base
from data_management.game_data_service import GameDataService


class LogMessage:
    def __init__(self, canvas, log_id: int, duration: int, spacing: float):
        self.canvas = canvas

        self.id = log_id
        self.duration = duration
        self.spacing = spacing

        self.time = 0

    def increase_time(self):
        self.time +=1

    def expired(self) -> bool:
        return self.time > self.duration

    def move_up(self, offset):
        self.canvas.move(self.id, 0, - self.spacing * offset)

    def delete(self, logs: dict):
        self.canvas.delete(self.id)

        del logs[self.id]


class LogList(Base):
    def __init__(
            self, data: GameDataService, window_name, window, width: float, height: float, canvas
    ):
        super().__init__(data, window_name, window, width, height, canvas)

        self.x0 = self.width * self.p().log_list_x0
        self.y0 = self.height * self.p().log_list_y0
        self.font = f"{self.p().main_font} {self.p().log_list_font_size}"

        self.vertical_spacing = self.height * self.p().log_list_vertical_spacing

        self.logs = {}

    def add_log(self, new_log: dict):
        # Add new log
        self._process_new_log(new_log)

    def delete_expired_logs(self):
        logs_to_delete = []

        # Increase amount of time logs have been active
        for log_id, log in self.logs.items():
            log.increase_time()

            # Check which logs have expired
            if log.expired():
                logs_to_delete.append(log_id)

        # Delete expired logs
        for to_delete in logs_to_delete:
            self.logs[to_delete].delete(self.logs)

        # Move the remaining logs up
        for log_id, log in self.logs.items():
            log.move_up(offset=len(logs_to_delete))

    def _process_new_log(self, new_log: dict):
        # Get log type
        log_type = new_log["type"]

        # Get aircraft
        aircraft = new_log["aircraft"]

        # Get parameters
        message, fill, duration = getattr(self, f"_prepare_{log_type}_log")(aircraft)

        # Add log
        self._add_log(message, fill, duration)

    def _prepare_dep_ready_log(self, aircraft) -> Tuple[str, str, int]:
        # Get current period of the day
        now = datetime.utcnow()
        period = [per["t"] for per in self.p().day_periods.values() if per["h"][0] <= now.hour <= per["h"][1]][0]

        # Prepare message
        message = self.p().log_list_msg_dep_ready.format(
            flight_no=aircraft.flight_no, period=period, rwy=aircraft.runway.get_name()
        )

        # Get colour
        fill = self.p().log_list_info_colour

        return message, fill, self.p().log_list_duration

    def _prepare_arr_ready_log(self, aircraft) -> Tuple[str, str, int]:
        # Get current period of the day
        now = datetime.utcnow()
        period = [per["t"] for per in self.p().day_periods.values() if per["h"][0] <= now.hour <= per["h"][1]][0]

        # Prepare message
        message = self.p().log_list_msg_arr_ready.format(
            flight_no=aircraft.flight_no, period=period, alt=int(aircraft.altitude), hdg=int(aircraft.heading)
        )

        # Get colour
        fill = self.p().log_list_info_colour

        return message, fill, self.p().log_list_duration

    def _prepare_dep_takeoff_invalid_spd_hdg_log(self, aircraft) -> Tuple[str, str, int]:
        # Prepare message
        message = self.p().log_list_dep_takeoff_invalid_spd_hdg.format(flight_no=aircraft.flight_no)

        # Get colour
        fill = self.p().log_list_warn_colour

        return message, fill, self.p().log_list_duration

    def _add_log(self, message: str, fill: str, duration: int):
        log_id = self.canvas.create_text(
            self.x0,
            self.y0 + self._get_total_vertical_displacement(),
            fill=fill,
            font=self.font,
            text=message,
            anchor="w"
        )

        self.logs[log_id] = (LogMessage(self.canvas, log_id, duration, self.vertical_spacing))

    def _get_total_vertical_displacement(self) -> float:
        return self._get_log_list_size() * self.vertical_spacing

    def _get_log_list_size(self) -> int:
        return len(self.logs)
