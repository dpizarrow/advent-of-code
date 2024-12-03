from pathlib import Path
import sys
import re


def extract_muls(string: str):
    # Extract all sequences of the form mul(number, number)
    return re.findall(r"mul\((\d+),(\d+)\)", string)


def sub_do_dont(string: str):
    return re.sub(r"don't\(\)[\s\S]*?(?:do\(\)|$)", "", string)


def main(input_file: str):
    try:
        file_path = Path(input_file)

        if not file_path.is_file():
            print(f"Error: the file {input_file} does not exist")
            return

        with file_path.open("r", encoding="utf-8") as f:
            f = f.read()

        subbed_file = sub_do_dont(f)
        multiplications = extract_muls(subbed_file)
        result = sum([int(x) * int(y) for x, y in multiplications])
        print(f"Sum of multiplications is {result}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
