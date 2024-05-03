import abc


class OutputStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def output_data(self, filename: str, num_lines: int = -1) -> bool:
        raise NotImplementedError
