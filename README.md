# Kafka to MongoDB Pipeline

A simple Data Engineering project that consumes data from a remote Kafka cluster, republishes it to a local Kafka topic, and stores the data into MongoDB.

## Architecture

```text
                    Remote Kafka
             (product_view topic)
                        │
                        │ Consumer
                        ▼
                 producer.py
      (Consumer + Producer / Forwarder)
                        │
                        ▼
              Local Kafka Cluster
          (product_view_local topic)
                        │
                        │ Consumer
                        ▼
                  consumer.py
                        │
                        ▼
                    MongoDB
```

---

## Tech Stack

- Python 3.12
- Apache Kafka
- Confluent Kafka Python
- MongoDB
- Docker
- AKHQ
- python-dotenv

---

## Project Structure

```
kafka-mongo/
│
├── producer.py
├── consumer.py
├── config.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Features

- Consume messages from a remote Kafka topic.
- Produce messages to a local Kafka topic.
- Consume messages from the local Kafka topic.
- Store JSON documents into MongoDB.
- Environment-based configuration.

---

## Prerequisites

- Python 3.12+
- Docker
- MongoDB
- Local Kafka Cluster
- AKHQ (optional)

---

## Installation

Clone repository

```bash
git clone <repository-url>
cd kafka-mongo
```

Create virtual environment

```bash
python -m venv .venv
```

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
# Remote Kafka
REMOTE_KAFKA_BOOTSTRAP_SERVERS=46.xxx.xxx.xxx:9094
REMOTE_KAFKA_SECURITY_PROTOCOL=SASL_PLAINTEXT
REMOTE_KAFKA_SASL_MECHANISM=PLAIN
REMOTE_KAFKA_USERNAME=*****
REMOTE_KAFKA_PASSWORD=*****
REMOTE_KAFKA_TOPIC=product_view

# Local Kafka
LOCAL_KAFKA_BOOTSTRAP_SERVERS=localhost:9094
LOCAL_KAFKA_SECURITY_PROTOCOL=SASL_PLAINTEXT
LOCAL_KAFKA_SASL_MECHANISM=PLAIN
LOCAL_KAFKA_USERNAME=*****
LOCAL_KAFKA_PASSWORD=*****
LOCAL_KAFKA_TOPIC=product_view_local

# Consumer
CONSUMER_GROUP_ID=product_view_group
AUTO_OFFSET_RESET=earliest

# MongoDB
MONGO_URI=mongodb://localhost:27017
MONGO_DATABASE=kafka_lab
MONGO_COLLECTION=product_view
```

---

## Run

### Start Kafka

Start your local Kafka cluster.

Create topic

```
product_view_local
```

---

### Start Producer

```bash
python producer.py
```

The producer:

- Consumes data from the remote Kafka topic.
- Produces data into the local Kafka topic.

---

### Start Consumer

```bash
python consumer.py
```

The consumer:

- Reads messages from the local Kafka topic.
- Parses JSON data.
- Inserts documents into MongoDB.

---

## MongoDB

Verify inserted documents

```javascript
use kafka_lab

db.product_view.findOne()

db.product_view.countDocuments()
```

---

## Kafka Configuration

Local topic

| Property | Value |
|----------|------|
| Topic | product_view_local |
| Partitions | 3 |
| Replication Factor | 1 |

---

## Dependencies

```
confluent-kafka
pymongo
python-dotenv
```

or

```bash
pip install -r requirements.txt
```

---
