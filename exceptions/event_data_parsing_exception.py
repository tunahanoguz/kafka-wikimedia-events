class EventDataParsingException(Exception):
    def __init__(self, msg):
        super().__init__(f"There is an event data parsing error! {msg}")
