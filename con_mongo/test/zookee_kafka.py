#!/usr/bin/env python
#encoding:utf8
#author: zeping lai
from pykafka import KafkaClient
client = KafkaClient(hosts="10.3.236.223:9092")
topic = client.topics['test']
balanced_consumer= topic.get_balanced_consumer(
    consumer_group='linuxhub',
    auto_commit_enable=True,
#    reset_offset_on_start=True,
    zookeeper_connect='10.3.236.223:2181'
)
for message in balanced_consumer:
    if message is not None:
        print message.offset, message.value