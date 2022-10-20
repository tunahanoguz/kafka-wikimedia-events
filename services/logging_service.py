import os
import logging
from logging.handlers import RotatingFileHandler
from logging import Logger
from configs import ConfigFileParser


class LoggingService:
    def __init__(self, region: str):
        self._region = region
        self._get_config()
        self._create_logs_dir()

    def _get_config(self):
        config_parser = ConfigFileParser('logging_config.yaml')
        self._logging_config = config_parser.parse()[self._region]

    def _create_logs_dir(self):
        self._root_dir = os.path.dirname(os.path.dirname(__file__))
        self._log_dir = os.path.join(self._root_dir, "logs")
        if not os.path.exists(self._log_dir):
            os.mkdir(self._log_dir)

    def create_logging(self) -> Logger:
        kafka_logging = logging.getLogger(__name__)
        kafka_logging.setLevel(logging.INFO)

        logging_handler = RotatingFileHandler(filename=self._log_dir + '/' + self._logging_config['file_name'],
                                              maxBytes=int(self._logging_config['max_bytes']),
                                              backupCount=int(self._logging_config['backup_count']))

        logging_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        logging_handler.setFormatter(logging_formatter)
        kafka_logging.addHandler(logging_handler)
        return kafka_logging

