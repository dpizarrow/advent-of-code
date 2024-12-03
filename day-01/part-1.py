from pathlib import Path
import sys


def main(input_file: str):
    try:
        left_list, right_list = [], []
        file_path = Path(input_file)

        if not file_path.is_file():
            print(f"Error: the file {input_file} does not exist")
            return

        with file_path.open("r", encoding="utf-8") as f:
            for line in f.readlines():
                l, r = line.split("   ")
                left_list.append(int(l))
                right_list.append(int(r))

        left_list = sorted(left_list)
        right_list = sorted(right_list)

        total_distance = sum([abs(x - y) for x, y in zip(left_list, right_list)])
        print(f"Total distance is {total_distance}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
