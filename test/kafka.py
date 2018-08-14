import logging
import logger
from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.0.245:9092")
logging.info(client.topics)

topic = client.topics[('Hello-Kafka').encode()]

producer=topic.get_sync_producer()
while True:
    event = input("Add what to event log?: ('Q' to end.): ").encode()
    if event == 'Q':
        break
    else:
       # msg = event.encode('UTF-8', 'ignore')

        producer.produce(event)