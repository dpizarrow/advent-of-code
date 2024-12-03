from pathlib import Path
import sys
from collections import Counter


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

        times_in_right_list = Counter(right_list)
        similarities = [x * times_in_right_list[x] for x in left_list]
        similarity_score = sum(similarities)
        print(f"Similarity score is {similarity_score}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python part-1.py <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
