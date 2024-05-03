class OutputContext:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def output_data(self, filename: str, num_lines: int) -> bool:
        if not self.strategy:
            raise ValueError('Strategy not set')
        return self.strategy.output_data(filename, num_lines)
