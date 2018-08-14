# -*- coding:utf-8 -*-
from pykafka import KafkaClient


client = KafkaClient(hosts='10.3.236.223:9092,10.3.236.224:9092,10.3.236.225:9092')
topic = client.topics['Multibrokerapp']


balanced_consumer = topic.get_balanced_consumer(
    auto_commit_enable=False,
    zookeeper_connect='10.3.236.223:2181,10.3.236.224:2181,10.3.236.225:2181'
)

for message in balanced_consumer:
    if message is not None:
        print message.offset, message.value