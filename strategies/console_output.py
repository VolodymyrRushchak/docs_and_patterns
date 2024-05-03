from strategies.output_strategy import OutputStrategy
import csv


class ConsoleOutput(OutputStrategy):

    def output_data(self, filename: str, num_lines: int = -1) -> bool:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            lines_printed = 0
            for row in reader:
                print(row)
                lines_printed += 1
                if num_lines != -1 and lines_printed == num_lines:
                    return True
        if num_lines == -1:
            return True
        return False
