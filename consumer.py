from concurrent.futures import ThreadPoolExecutor
from context_managers import ConsumerContextManager
from services import ConsumerService

if __name__ == '__main__':
    consumer_cxm = ConsumerContextManager()
    consumer_service = ConsumerService(consumer_cxm)
    with ThreadPoolExecutor() as executor:
        for i in range(1, 3):
            executor.submit(consumer_service.consume_message())
