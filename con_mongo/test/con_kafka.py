#!/usr/bin/python
# -*- coding:utf-8 -*-
from pykafka import KafkaClient

#kafka默认端口为9092
client = KafkaClient(hosts='110.3.236.223:9092')#这里连接多个客户端
topic = client.topics['test']

#从zookeeper消费，zookeeper的默认端口为2181
balanced_consumer = topic.get_balanced_consumer(
    consumer_group='test_kafka_group',
    auto_commit_enable=True,  # 设置为False的时候不需要添加consumer_group，直接连接topic即可取到消息
    zookeeper_connect='10.3.236.223:2181'#这里就是连接多个zk
)

for message in balanced_consumer:
    # print message
    if message is not None:
        print (message.offset, message.value)#打印接收到的消息体的偏移个数和值