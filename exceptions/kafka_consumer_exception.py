class KafkaConsumerException(Exception):
    def __init__(self, msg):
        super().__init__(f"There is an error related to Kafka consumer: {msg}")
