from pathlib import Path
import sys
from functools import cmp_to_key


def check_correct_order(page, rules_dict):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            rule_key = (page[i], page[j])
            if rule_key in rules_dict:
                if rules_dict[rule_key] != 1:  # If the order is not as expected
                    return False
    return True


def compare(a, b, rules_dict):
    if (a, b) in rules_dict:
        return rules_dict[(a, b)]
    elif (b, a) in rules_dict:
        return -rules_dict[(b, a)]
    return 0


def main(input_file: str):
    total = 0
    file_path = Path(input_file)
    if not file_path.is_file():
        print(f"Error: the file {input_file} does not exist")
        return

    try:
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        separator = lines.index("")
        rules = [[int(x) for x in rule.split("|")] for rule in lines[0:separator]]
        pages = [
            [int(x) for x in line.split(",")]
            for line in lines[separator + 1 :]
            if line.strip()
        ]

        rules_dict = {}
        for a, b in rules:
            rules_dict[(a, b)] = 1
            rules_dict[(b, a)] = -1

        for page in pages:
            if not check_correct_order(page, rules_dict):
                page.sort(key=cmp_to_key(lambda x, y: compare(x, y, rules_dict)))
                total += page[len(page) // 2]

        print(f"Total is {total}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input_file>")
        sys.exit(1)

    main(sys.argv[1])
