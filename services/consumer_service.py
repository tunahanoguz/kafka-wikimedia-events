from kafka.consumer.fetcher import ConsumerRecord
from context_managers import ConsumerContextManager
from concurrent.futures import ThreadPoolExecutor
from models import WikimediaEvent
import json


class ConsumerService:
    def __init__(self, consumer_context_manager: object):
        self._consumer_cxm = consumer_context_manager

    def consume_message(self):
        with self._consumer_cxm as p:
            for message in p:
                print(self._parse_message(message))
                p.commit()

    @staticmethod
    def _parse_message(message: ConsumerRecord) -> WikimediaEvent:
        message_json = json.loads(message.value.decode('utf8').replace("'", '"'))
        return WikimediaEvent(**message_json)


if __name__ == '__main__':
    consumer_cxm = ConsumerContextManager()
    consumer_service = ConsumerService(consumer_cxm)
    with ThreadPoolExecutor() as executor:
        for i in range(1, 3):
            executor.submit(consumer_service.consume_message())
