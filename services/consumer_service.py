from kafka.consumer.fetcher import ConsumerRecord
from models import WikimediaEvent
from services.logging_service import LoggingService
from exceptions import EventDataParsingException
import json


class ConsumerService:
    def __init__(self, consumer_context_manager: object):
        self._consumer_cxm = consumer_context_manager
        logging_service = LoggingService('producer')
        self._logging = logging_service.create_logging()

    def consume_message(self):
        try:
            with self._consumer_cxm as p:
                for message in p:
                    print(self._parse_message(message))
                    p.commit()
        except Exception as e:
            self._logging.exception(e)
            pass

    @staticmethod
    def _parse_message(message: ConsumerRecord) -> WikimediaEvent:
        try:
            message_json = json.loads(message.value.decode('utf8').replace("'", '"'))
            return WikimediaEvent(**message_json)
        except Exception as e:
            raise EventDataParsingException(e)
