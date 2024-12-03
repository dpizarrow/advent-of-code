from pathlib import Path
import sys


def main(input_file: str):
    try:
        pass

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
