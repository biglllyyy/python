#!/usr/bin/env python
#encoding:utf8
#author: zeping lai
from pykafka import KafkaClient
client = KafkaClient(hosts="10.3.236.223:9092")
topic = client.topics['test']
consumer = topic.get_simple_consumer(
    consumer_group="linuxhub",
#    auto_offset_reset=OffsetType.EARLIEST,
    reset_offset_on_start=True
)
for message in consumer:
    if message is not None:
        print message.offset, message.value