from confluent_kafka import Consumer, Producer
from confluent_kafka.error import KafkaException

from config import (
    REMOTE_KAFKA_CONFIG,
    LOCAL_KAFKA_CONFIG,
    REMOTE_TOPIC,
    LOCAL_TOPIC,
)

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(
            f"Message sent to {msg.topic()} "
            f"[Partition {msg.partition()}] @ Offset {msg.offset()}"
        )


def main():
    consumer = Consumer(REMOTE_KAFKA_CONFIG)
    producer = Producer(LOCAL_KAFKA_CONFIG)

    consumer.subscribe([REMOTE_TOPIC])

    print(f"Listening topic '{REMOTE_TOPIC}'...")
    print(f"Forwarding to '{LOCAL_TOPIC}'...\n")

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                raise KafkaException(msg.error())

            producer.produce(
                topic=LOCAL_TOPIC,
                key=msg.key(),
                value=msg.value(),
                callback=delivery_report,
            )

            producer.poll(0)

    except KeyboardInterrupt:
        print("\nStopping producer...")

    finally:
        consumer.close()
        producer.flush()


if __name__ == "__main__":
    main()