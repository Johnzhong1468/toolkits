import datetime
import os
import logging
from logging.handlers import TimedRotatingFileHandler
import json
from src.definitions import LOGS_DIR


class ProjectLogger:

    DEFAULT = "src"
    LOGS_ENABLED = True
    CONSOLE_PRINT_ENABLED = True
    REALTIME_WRITING_ENABLED = False
    REALTIME_WRITING_PATH = None
    FILE_BACKUP_COUNT = 60
    LOG_FORMAT = "[%(asctime)s] %(levelname)s - %(message)s"

    LOGGERS = {}
    LOG_DATA = []
    LOG_TIME = []

    def __init__(self, name = None):
        self.log_data = []
        self.log_time = []
        self.logger_name = self.DEFAULT if name is None else name
        self.logger_obj = self.log_set_up(self.logger_name)

    @classmethod
    def get_logger(cls, name):
        return cls(name)

    @classmethod
    def close_handlers(cls, logger_obj):
        [handle.close() for handle in logger_obj.handlers]

    @staticmethod
    def log_set_up(log_name):
        if ProjectLogger.LOGGERS.get(log_name):
            return ProjectLogger.LOGGERS.get(log_name)
        logger = logging.getLogger(log_name)

        # default
        default_log_file = f"{ProjectLogger.DEFAULT}.log"
        default_log_dir = LOGS_DIR
        os.makedirs(default_log_dir, exist_ok=True)
        default_log_path = os.path.join(default_log_dir, default_log_file)
        default_handler = TimedRotatingFileHandler(default_log_path, when="midnight", backupCount=ProjectLogger.FILE_BACKUP_COUNT)
        default_handler.setFormatter(logging.Formatter(ProjectLogger.LOG_FORMAT))
        logger.addHandler(default_handler)

        if log_name != ProjectLogger.DEFAULT:
            log_file = f"{log_name}.log"
            log_dir = os.path.join(LOGS_DIR, log_name)
            os.makedirs(log_dir, exist_ok=True)
            log_path = os.path.join(log_dir, log_file)
            handler = TimedRotatingFileHandler(log_path, when="midnight", backupCount=ProjectLogger.FILE_BACKUP_COUNT)
            handler.setFormatter(logging.Formatter(ProjectLogger.LOG_FORMAT))
            logger.addHandler(handler)

        logger.setLevel(logging.INFO)
        ProjectLogger.close_handlers(logger)
        ProjectLogger.LOGGERS[log_name] = logger
        return logger

    def logger(self, *log_strings, level="INFO", print_stdout=True):
        log_string = " ".join([str(l) for l in log_strings])
        if ProjectLogger.LOGS_ENABLED:
            self.log_message(log_string, level)
        if self.CONSOLE_PRINT_ENABLED and print_stdout:
            print(log_string)

        self.log_data.append(log_string)
        ProjectLogger.LOG_DATA.append(self.log_data[-1])
        self.log_time.append(str(datetime.datetime.now()))
        ProjectLogger.LOG_TIME.append(self.log_time[-1])

        if ProjectLogger.REALTIME_WRITING_ENABLED and ProjectLogger.REALTIME_WRITING_PATH is not None:
            if os.path.exists(ProjectLogger.REALTIME_WRITING_PATH):
                with open(ProjectLogger.REALTIME_WRITING_PATH) as json_log:
                    data = json.load(json_log)
            else:
                data = {}
            data[self.log_time[-1]] = self.log_data[-1]

            with open(ProjectLogger.REALTIME_WRITING_PATH, "w") as json_log:
                json.dump(data, json_log)

    @staticmethod
    def flush_logs():
        ProjectLogger.LOG_DATA = []
        ProjectLogger.LOG_TIME = []

    @staticmethod
    def to_json():
        return dict(zip(ProjectLogger.LOG_TIME, ProjectLogger.LOG_DATA))

    @staticmethod
    def write_to_file(directory):
        file_name = f"LogRequest_{str(datetime.datetime.now())}.json"
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, file_name), "w") as log_file:
            json.dump(ProjectLogger.to_json(), log_file)

    def log_message(self, log_string, level):
        try:
            getattr(self.logger_obj, level.lower())(log_string)
            ProjectLogger.close_handlers(self.logger_obj)
        except PermissionError:
            self.log_message()


LOG = ProjectLogger()
