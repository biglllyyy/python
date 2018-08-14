from pykafka import KafkaClient
client = KafkaClient(hosts="10.3.236.223:9092")
print client.topics