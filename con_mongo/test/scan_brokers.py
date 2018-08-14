from pykafka import KafkaClient
client = KafkaClient(hosts="10.3.236.223:9092")
print "client.brokers is :"+str(client.brokers)
for n in client.brokers:
    host = client.brokers[n].host
    port = client.brokers[n].port
    id = client.brokers[n].id
    print "host=%s | port=%s | broker.id=%s " %(host,port,id)