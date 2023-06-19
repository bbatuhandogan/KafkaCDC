from kafka import KafkaProducer
from pymongo import MongoClient
import json
import time
import schedule

# MongoDB configurations
mongo_host = 'mongodb://localhost:27017'
mongo_db = 'CDC_database'
mongo_collection = 'CDC_collection'

# Kafka configurations
kafka_bootstrap_servers = ['localhost:9092']
kafka_topic = 'default'

# Connect to MongoDB
client = MongoClient(mongo_host)
db = client[mongo_db]
collection = db[mongo_collection]

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# This function continuously queries a MongoDB collection for new documents (those added after the last processed document), and sends them to a Kafka topic.
def process_new_documents(collection, producer, kafka_topic, sleep_interval: Optional[int] = 10):
    """
    :param collection: MongoDB collection object to query for new documents.
    :param producer: Kafka producer to send new documents.
    :param kafka_topic: Kafka topic to which new documents should be sent.
    :param sleep_interval: Time (in seconds) the function should sleep before checking for new documents again. Defaults to 10.
    """
    
    # Initialize the variable to keep track of the last processed document ID
    last_document_id = None

    while True:
        # Prepare the MongoDB query
        query = {}
        if last_document_id:
            # If there is a last processed document ID, get documents with ID greater than this
            query['_id'] = {'$gt': last_document_id}

        # Query the MongoDB collection
        new_documents = collection.find(query)

        for doc in new_documents:
            # Prepare the Kafka message
            message = {'document': doc}

            # Send the message to the Kafka topic
            producer.send(kafka_topic, value=message)

            # Update the last processed document ID
            last_document_id = doc['_id']

        # Sleep for the specified interval before checking for new documents again
        time.sleep(sleep_interval)

if __name__ == '__main__':
    process_new_documents(collection=collection, producer=producer, kafka_topic=kafka_topic)