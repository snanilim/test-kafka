from kafka import KafkaProducer
from time import sleep
from json import dumps

try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))

try:
    for e in range(10):
        data = {'number' : e}
        producer.send('test', value=data)
        sleep(1)
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))
