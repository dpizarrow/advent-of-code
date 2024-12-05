from pathlib import Path
import sys

DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


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
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != "X":
                continue
            for dr, dc in DIRECTIONS:
                if not (0 <= row + 3 * dr < rows and 0 <= col + 3 * dc < cols):
                    continue
                if (
                    grid[row + dr][col + dc] == "M"
                    and grid[row + 2 * dr][col + 2 * dc] == "A"
                    and grid[row + 3 * dr][col + 3 * dc] == "S"
                ):
                    result += 1

    print(f"Number of results: {result}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
