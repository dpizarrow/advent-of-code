from pathlib import Path
import sys


def check_correct_order(page, rules_dict):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            rule_key = (page[i], page[j])
            if rule_key in rules_dict and not rules_dict[rule_key]:
                return False
    return True


def main(input_file: str):
    total = 0
    file_path = Path(input_file)
    try:
        if not file_path.is_file():
            print(f"Error: the file {input_file} does not exist")
            return

        with file_path.open("r", encoding="utf-8") as f:
            f = f.read()

        f = f.splitlines()
        separator = f.index("")
        rules = f[0:separator]
        rules = [[int(rule.split("|")[0]), int(rule.split("|")[1])] for rule in rules]

        pages = f[separator + 1 :]
        pages = [line for line in pages if line.strip()]
        pages = [list(map(int, line.split(","))) for line in pages]

        rules_dict = {}
        for a, b in rules:
            rules_dict[(a, b)] = True
            rules_dict[(b, a)] = False

        for page in pages:
            if check_correct_order(page, rules_dict):
                total += page[len(page) // 2]
        print(f"Total is {total}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <path_to_input>")
        sys.exit(1)

    input_file = sys.argv[1]

    main(input_file)
