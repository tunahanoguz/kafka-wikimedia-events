from dataclasses import dataclass, field
from datetime import datetime


@dataclass()
class WikimediaEvent:
    id: str
    uri: str
    request_id: str
    domain: str
    stream: str
    event_date: datetime = field(default=datetime.now())
