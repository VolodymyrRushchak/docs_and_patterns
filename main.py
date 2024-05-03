from context import OutputContext
from strategies.console_output import ConsoleOutput
from strategies.kafka_output import KafkaOutput
import yaml


if __name__ == '__main__':
    with open('resources/config.yml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    context = OutputContext(KafkaOutput(topic='fire-incident-events') if config['kafka_output'] else ConsoleOutput())
    print('Success: ', context.output_data('resources/data/Fire_Incident_Dispatch_Data_20240502.csv', 10))
