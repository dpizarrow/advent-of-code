from pathlib import Path
import sys


def main(input_file: str):
    file_path = Path(input_file)
    try:
        if not file_path.is_file():
            print(f"Error: the file {input_file} does not exist")
            return

        with file_path.open("r", encoding="utf-8") as f:
            f = f.read()

        grid = list(line for line in f.splitlines())
        rows = len(grid)
        cols = len(grid[0])
        start_pos = None
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char == "^":
                    start_pos = (r, c)
                    break
            if start_pos:
                break
        row_step = -1
        col_step = 0
        seen = set()
        while True:
            seen.add((r, c))
            if (
                r + row_step < 0
                or r + row_step >= rows
                or c + col_step < 0
                or c + col_step >= cols
            ):
                break
            if grid[r + row_step][c + col_step] == "#":
                row_step, col_step = col_step, -row_step
            else:
                r += row_step
                c += col_step
        print(f"Guard visited {len(seen)} positions")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
