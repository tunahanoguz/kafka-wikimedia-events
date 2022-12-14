from sseclient import SSEClient as EventSource
from configs import ConfigFileParser
from models import WikimediaEvent
from services.logging_service import LoggingService
from exceptions import InvalidEventDataException, EventDataParsingException
import json


class ProducerService:
    def __init__(self, producer_context_manager: object):
        self._producer_cxm = producer_context_manager
        config_parser = ConfigFileParser('kafka_config.yaml')
        self._kafka_config = config_parser.parse()
        logging_service = LoggingService('producer')
        self._logging = logging_service.create_logging()

    def send_message(self, topic: str, key: str, data: WikimediaEvent):
        with self._producer_cxm as p:
            data = data.__dict__
            if '_sa_instance_state' in data.keys():
                data.pop('_sa_instance_state')
            p.send(topic, key=bytes(key, encoding='utf-8'), value=bytes(str(data), encoding='utf-8'))

    def send_wikimedia_events(self):
        stream_url = 'https://stream.wikimedia.org/v2/stream/recentchange'
        for (idx, event) in enumerate(EventSource(stream_url)):
            try:
                if event.event != 'message' or event.data is None or len(event.data) == 0:
                    raise InvalidEventDataException

                wikimedia_event = self._parse_event_data(event.data)
                self.send_message(self._kafka_config['topic'], str(idx), wikimedia_event)
            except Exception as e:
                self._logging.exception(e)
                pass

    @staticmethod
    def _parse_event_data(data):
        try:
            event_meta = json.loads(data)['meta']
            return WikimediaEvent(id=event_meta['id'],
                                  uri=event_meta['uri'],
                                  request_id=event_meta['request_id'],
                                  domain=event_meta['domain'],
                                  stream=event_meta['stream'],
                                  event_date=event_meta['dt'])
        except Exception as e:
            raise EventDataParsingException(e)
