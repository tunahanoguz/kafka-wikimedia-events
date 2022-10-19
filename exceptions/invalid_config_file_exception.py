class InvalidConfigFileException(Exception):
    def __init__(self):
        super().__init__("Config file is invalid!")
