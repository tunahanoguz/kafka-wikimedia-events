from kafka import KafkaConsumer
from configs import ConfigFileParser
from exceptions import ConfigFileNotFoundException, InvalidConfigFileException, KafkaConsumerException


class ConsumerContextManager:
    def __enter__(self):
        try:
            config_parser = ConfigFileParser('kafka_config.yaml')
            kafka_config = config_parser.parse()
            self._producer = KafkaConsumer(kafka_config['topic'], **kafka_config['consumer'])
            return self._producer
        except (ConfigFileNotFoundException, InvalidConfigFileException):
            raise
        except Exception as e:
            raise KafkaConsumerException(e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._producer.close()
        except Exception as e:
            raise KafkaConsumerException(e)
