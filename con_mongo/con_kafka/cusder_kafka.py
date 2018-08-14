#!/usr/bin/python
# -*- coding:utf-8 -*-

from pykafka import KafkaClient

client = KafkaClient(hosts="192.168.0.245:9092")  # 可接受多个client
# 查看所有的topic
client.topics
print (client.topics)

topic = client.topics[('Hello-Kafka')]  # 选择一个topic

message = "test message test message"
# 当有了topic之后呢，可以创建一个producer,来发消息，生产kafka数据,通过字符串形式，
with topic.get_sync_producer() as producer:
    producer.produce(message)
# The example above would produce to kafka synchronously -
# the call only returns after we have confirmation that the message made it to the cluster.
# 以上的例子将产生kafka同步消息，这个调用仅仅在我们已经确认消息已经发送到集群之后

# 但生产环境，为了达到高吞吐量，要采用异步的方式，通过delivery_reports =True来启用队列接口；
with topic.get_sync_producer() as producer:
    producer.produce('test message', partition_key='{}')
producer = topic.get_producer()
producer.produce(message)
print (message)