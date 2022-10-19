It's a project written in Python that handles Wikimedia "recent change" events and produces and consumes them with Apache Kafka.

## 🔗 Requirements
- kafka-python
- sseclient
- pyyaml

```bash
pip install -r requirements.txt
```

## 🛠 Configuration

There are `configs` folder in root directory of the project. The most **important** configuration file is `kafka_config.ini` file. You can edit this file according to your Apache Kafka configs.

## 🛡 Legal Notes

This project is purely for educational purposes. The data obtained is not processed anywhere and is not used for commercial purposes.