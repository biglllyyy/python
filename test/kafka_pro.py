from pykafka import KafkaClient
from tornado.options import options


def handle_request(request_topic_name, customer_group, response_topic_name):
    """
    处理接入服务发送到kafka内供解析服务来处理的原始数据
    """
    # 处理
    request_client = KafkaClient(hosts=options.kafka_connect, use_greenlets=True)
    request_topic = request_client.topics[request_topic_name]
    request_consumer = request_topic.get_balanced_consumer(consumer_group=customer_group,
                                                           auto_commit_enable=True,
                                                           zookeeper_connect=options.zookeeper_connect)
    # 回应
    response_client = KafkaClient(hosts=options.kafka_connect, use_greenlets=True)
    response_topic = response_client.topics[response_topic_name]
    response_producer = response_topic.get_producer()

    return request_consumer, response_producer


def transfer_raw(raw_topic_name):
    """
    发送原始数据到kafka，待后续上报服务、存储服务来使用
    """
    raw_client = KafkaClient(hosts=options.kafka_connect, use_greenlets=True)
    raw_topic = raw_client.topics[raw_topic_name]
    raw_producer = raw_topic.get_producer()
    return raw_producer

