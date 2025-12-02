
import importlib


def main():
    day_part = input("input day and part number to run\n")
    module = importlib.import_module(f"day{day_part[:-1]}.part{day_part[-1]}")
    module.solve()


if __name__ == "__main__":
    main()
