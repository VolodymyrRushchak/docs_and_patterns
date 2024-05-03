from strategies.output_strategy import OutputStrategy
import csv
from confluent_kafka import Producer
import socket


class KafkaOutput(OutputStrategy):
    def __init__(self, topic: str):
        conf = {'bootstrap.servers': 'localhost:9092',
                'client.id': socket.gethostname()}
        self.producer = Producer(conf)
        self.topic = topic

    def output_data(self, filename: str, num_lines: int = -1) -> bool:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines_sent = 0
            next(reader)
            for row in reader:
                self.producer.produce(self.topic, key="fire_incident", value=', '.join(row))
                lines_sent += 1
                if num_lines != -1 and lines_sent == num_lines:
                    break
        self.producer.flush()
        return True

