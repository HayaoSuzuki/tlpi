import os


def main():
    for key, value in os.environ.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
