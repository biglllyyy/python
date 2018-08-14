# -*- coding:utf-8 -*-
import datetime
from pykafka import KafkaClient
def con_kafka(kafka_host,zk_host):
    count=0
    #kafka默认端口为9092
    client = KafkaClient(hosts=kafka_host)#这里连接多个客户端
    topic = client.topics['login']

    #从zookeeper消费，zookeeper的默认端口为2181
    balanced_consumer = topic.get_balanced_consumer(
        consumer_group='test_kafka_group',
        auto_commit_enable=True,  # 设置为False的时候不需要添加consumer_group，直接连接topic即可取到消息
        zookeeper_connect=zk_host#这里就是连接多个zk
    )

    for message in balanced_consumer:
        # print message
        count+=1
        if message is not None:
            print message.offset, message.value#打印接收到的消息体的偏移个数和值
        if count==1:
            print "kafka con is error"


if __name__ == '__main__':
    kafka_host='10.2.23.8:4303'
    zk_host='10.2.23.8:4304'
    args=(kafka_host,zk_host)
    con_kafka(*args)