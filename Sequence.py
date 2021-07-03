from pathlib import Path


class Sequence:
    text = ""

    def __init__(self, seq_name):
        self.seq_name = seq_name

    def add_line(self, line):
        self.text += line

    def save_to_file(self, path, extension="txt"):
        Path(path).mkdir(parents=True, exist_ok=True)
        with open(
            "{}{}.{}".format(path, self.seq_name, extension),
            "w",
            encoding="utf8"
        ) as output_file:
            output_file.write(self.text)
            output_file.close()
