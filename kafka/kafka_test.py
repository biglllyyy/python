# -*- coding:utf-8 -*-

from pykafka import KafkaClient

client = KafkaClient(hosts="10.3.236.223:9092,10.3.236.224:9092,10.3.236.225:9092")

client.topics
print client.topics

topic = client.topics['Multibrokerapp']

message = "test message test message"

with topic.get_sync_producer() as producer:
    producer.produce(message)

with topic.get_sync_producer() as producer:
    producer.produce('test message', partition_key='{}')
producer = topic.get_producer()
producer.produce(message)
print message