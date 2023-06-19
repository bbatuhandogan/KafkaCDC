from kafka import KafkaConsumer
import json

# Kafka configurations
kafka_bootstrap_servers = ['localhost:9092']
kafka_topic = 'default'

# Create Kafka consumer
consumer = KafkaConsumer(
     kafka_topic,
     bootstrap_servers=kafka_bootstrap_servers,
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Consume Messages from Kafka
def consume_messages():
    for message in consumer:
        print(message.value)

if __name__ == '__main__':
    consume_messages()
