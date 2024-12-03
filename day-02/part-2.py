from pathlib import Path
import sys


def is_monotonic(lst: list):
    if len(lst) < 2:
        return True

    is_increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    is_decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    return is_increasing or is_decreasing


def check_level_difference(lst: list):
    return all(1 <= abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))


def main(input_file: str):
    try:
        file_path = Path(input_file)

        if not file_path.is_file():
            print(f"Error: the file {input_file} does not exist")
            return

        with file_path.open("r", encoding="utf-8") as f:
            lines = f.readlines()

        reports = [list(map(int, line.split())) for line in lines]
        safe_reports = 0
        for report in reports:
            if is_monotonic(report) and check_level_difference(report):
                safe_reports += 1
                continue
            for i in range(len(report)):
                dampened_report = report[:i] + report[i + 1 :]
                if is_monotonic(dampened_report) and check_level_difference(
                    dampened_report
                ):
                    safe_reports += 1
                    break

        print(f"Number of safe reports is {safe_reports}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
