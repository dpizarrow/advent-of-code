from pathlib import Path
import sys
import re


def main(input_file: str):
    file_path = Path(input_file)
    result = 0

    if not file_path.is_file():
        print(f"Error: the file {input_file} does not exist")
        return

    with file_path.open("r", encoding="utf-8") as f:
        f = f.read()

    grid = f.splitlines()
    rows = len(grid)
    cols = len(grid[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] != "A":
                continue
            corners = [
                grid[row - 1][col - 1],
                grid[row - 1][col + 1],
                grid[row + 1][col + 1],
                grid[row + 1][col - 1],
            ]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                result += 1

    print(f"Number of results: {result}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
