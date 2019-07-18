import os


def main():
    os.putenv("FOO", "BAR")
    os.environ["HOGE"] = "PIYO"
    for key, value in os.environ.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
