from kafka import KafkaProducer
from time import sleep
from json import dumps

try:
    producer = KafkaProducer(bootstrap_servers=['192.168.7.72:9092', '192.168.7.73:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))

try:
    for e in range(200):
        data = {'number' : e}
        producer.send('prTopic3.3', value=data)
        sleep(1)
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))

