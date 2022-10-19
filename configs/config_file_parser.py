import os
import yaml
from yaml.loader import SafeLoader
from yaml.error import YAMLError
from exceptions import ConfigFileNotFoundException, InvalidConfigFileException


class ConfigFileParser:
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    def parse(self):
        try:
            config_file_path = os.path.join(os.path.dirname(__file__), self._file_name)

            if not os.path.isfile(config_file_path):
                raise OSError

            with open(config_file_path) as f:
                db_config = yaml.load(f, Loader=SafeLoader)

            return db_config
        except OSError:
            raise ConfigFileNotFoundException
        except YAMLError:
            raise InvalidConfigFileException

    def __str__(self):
        return f"Config File Name: {self._file_name}"
