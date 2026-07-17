import json

from confluent_kafka import Consumer
from pymongo import MongoClient

from config import (
    LOCAL_KAFKA_CONFIG,
    LOCAL_TOPIC,
    MONGO_URI,
    MONGO_DATABASE,
    MONGO_COLLECTION,
)


def main():
    consumer = Consumer(LOCAL_KAFKA_CONFIG)
    consumer.subscribe([LOCAL_TOPIC])

    client = MongoClient(MONGO_URI)
    collection = client[MONGO_DATABASE][MONGO_COLLECTION]

    try:
        while True:
            msg = consumer.poll(0.1)

            if msg is None:
                continue

            if msg.error():
                print(f"Kafka Error: {msg.error()}")
                continue

            try:
                document = json.loads(msg.value().decode())

                collection.insert_one(document)

                consumer.commit(msg)

                print(
                    f"Inserted partition={msg.partition()} "
                    f"offset={msg.offset()}"
                )

            except Exception as e:
                print(f"Mongo Error: {e}")

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        consumer.close()
        client.close()


if __name__ == "__main__":
    main()