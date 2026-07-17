import os
from dotenv import load_dotenv

load_dotenv()

REMOTE_KAFKA_CONFIG = {
    "bootstrap.servers": os.getenv("REMOTE_KAFKA_BOOTSTRAP_SERVERS"),
    "security.protocol": os.getenv("REMOTE_KAFKA_SECURITY_PROTOCOL"),
    "sasl.mechanism": os.getenv("REMOTE_KAFKA_SASL_MECHANISM"),
    "sasl.username": os.getenv("REMOTE_KAFKA_USERNAME"),
    "sasl.password": os.getenv("REMOTE_KAFKA_PASSWORD"),
    "auto.offset.reset": os.getenv("AUTO_OFFSET_RESET"),
}

LOCAL_KAFKA_CONFIG = {
    "bootstrap.servers": os.getenv("LOCAL_KAFKA_BOOTSTRAP_SERVERS"),
    "security.protocol": os.getenv("LOCAL_KAFKA_SECURITY_PROTOCOL"),
    "sasl.mechanism": os.getenv("LOCAL_KAFKA_SASL_MECHANISM"),
    "sasl.username": os.getenv("LOCAL_KAFKA_USERNAME"),
    "sasl.password": os.getenv("LOCAL_KAFKA_PASSWORD"),
    "group.id": os.getenv("CONSUMER_GROUP_ID"),
    "auto.offset.reset": os.getenv("AUTO_OFFSET_RESET"),
}

REMOTE_TOPIC = os.getenv("REMOTE_KAFKA_TOPIC")
LOCAL_TOPIC = os.getenv("LOCAL_KAFKA_TOPIC")

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")