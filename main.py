# -*- coding: utf-8 -*-
import os
from pathlib import Path

from Sequence import Sequence


def unpack(file, destination_path):
    lines = file.readlines()

    during_sequence = False
    skip = 0
    for i, line in enumerate(lines):
        if skip > 0:
            skip -= 1

        # Timestamp - skip
        if line[0] == "=":
            continue

        # Blank line in sequence
        elif line[0] == "\n":
            # Blank line in text - add
            if i > 0 and lines[i-1][0] == "=" and lines[i+1][0] == "=":
                sequence.add_line(line)

        elif line[0] == ":":
            # End of sequence - Save
            if during_sequence:
                sequence.save_to_file(destination_path)
            # Start new sequence
            sequence = Sequence(line[2:-1])
            during_sequence = True
            skip = 1
        # Neutral line
        else:
            sequence.add_line(line)

    sequence.save_to_file(destination_path)


if __name__ == "__main__":
    input_path = input("Select game or subtitles folder absolute path: ")
    print("-------------------------------------------------------------")
    print("Searching files to extract...", end=" ")
    files = list(Path(input_path).rglob(r".\*.subtitles"))
    print("Done")
    print("Found {} files.".format(len(files)))

    output_path = input("Select destination folder: ")
    if output_path[:-1] != "\\":
        output_path += "\\"

    print("Unpacking files has been started...")
    for file in files:
        file_name = os.path.basename(file.name)
        print("Unpacking file {}".format(file_name))
        with open(file, "r", encoding="utf8") as input_file:
            destination_path = "{}\\{}\\".format(
                output_path,
                file_name.split(".")[0]
            )
            unpack(input_file, destination_path)
            input_file.close()

    input("\nPress enter to close program")
