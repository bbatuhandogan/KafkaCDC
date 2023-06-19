from pymongo.mongo_client import MongoClient

# MongoDB connection information
username = "batuhandogan"  # Username
password = "12345"  # Password

# MongoDB server addresses and port numbers
host1 = "ac-4alsji2-shard-00-00.6aljsz4.mongodb.net:27017"
host2 = "ac-4alsji2-shard-00-01.6aljsz4.mongodb.net:27017"
host3 = "ac-4alsji2-shard-00-02.6aljsz4.mongodb.net:27017"

# Database name and connection options
database = "mydatabase"  # Database name
ssl = "true"  # Use SSL
replica_set = "atlas-23zxc3-shard-0"  # Replica set name
auth_source = "admin"  # Authentication source
retry_writes = "true"  # Retry writes
write_concern = "majority"  # Write concern

# Constructing the connection string
uri = f"mongodb://{username}:{password}@{host1},{host2},{host3}/{database}?ssl={ssl}&replicaSet={replica_set}&authSource={auth_source}&retryWrites={retry_writes}&w={write_concern}"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("MongoDB connection succeed")
except Exception as e:
    print(e)

    