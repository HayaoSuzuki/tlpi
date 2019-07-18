import sys


def main():
    for idx, arg in enumerate(sys.argv):
        print(f"argv[{idx}] = {arg}")


if __name__ == "__main__":
    main()
