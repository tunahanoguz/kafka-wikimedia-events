from kafka import KafkaProducer
from configs import ConfigFileParser
from exceptions import ConfigFileNotFoundException, InvalidConfigFileException, KafkaProducerException


class ProducerContextManager:
    def __enter__(self):
        try:
            config_parser = ConfigFileParser('kafka_config.yaml')
            kafka_config = config_parser.parse()
            self._producer = KafkaProducer(bootstrap_servers=kafka_config['bootstrap_servers'])
            return self._producer
        except (ConfigFileNotFoundException, InvalidConfigFileException):
            raise
        except Exception as e:
            raise KafkaProducerException(e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._producer.flush()
        except Exception as e:
            raise KafkaProducerException(e)
