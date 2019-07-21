from kafka.admin import KafkaAdminClient, NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="192.168.7.72:9092", client_id='test')

topic_list = []
topic_list.append(NewTopic(name="prTopic2", num_partitions=2, replication_factor=2))
admin_client.create_topics(new_topics=topic_list, validate_only=False)