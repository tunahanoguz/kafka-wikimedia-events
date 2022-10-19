class ConfigFileNotFoundException(Exception):
    def __init__(self):
        super().__init__("Config file not found!")
