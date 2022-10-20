from concurrent.futures import ThreadPoolExecutor
from context_managers import ProducerContextManager
from services import ProducerService

if __name__ == '__main__':
    producer_cxm = ProducerContextManager()
    producer_service = ProducerService(producer_cxm)
    with ThreadPoolExecutor() as executor:
        for i in range(1, 11):
            executor.submit(producer_service.send_wikimedia_events)
