from confluent_kafka import Producer

# Kafka bootstrap servers and configuration
kafka_bootstrap_servers = 'kafka:9092'
kafka_topic = 'default'

producer_config = {
    'bootstrap.servers': kafka_bootstrap_servers
}

# Configure and start the Kafka producer
producer = Producer(producer_config)

# Message to be sent
message = "Hello world"

# Produce the message to the Kafka topic
producer.produce(kafka_topic, value=message.encode('utf-8'))

# Flush the buffer
producer.flush()

# Close the producer
producer.close()
