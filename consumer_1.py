from kafka import KafkaConsumer
from json import loads


consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['192.168.7.72:9092'],
    #  auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    message = message.value
    print(message)