import argparse
import os


def modify_env(environs):
    os.environ.clear()
    for arg in environs:
        key, value = arg.split("=")
        os.environ[key] = value

    if "GREET" not in os.environ:
        os.environ["GREET"] = "Hello world"

    if "BYE" in os.environ:
        del os.environ["BYE"]

    for key, value in os.environ.items():
        print(f"{key}={value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("environs", nargs="*")
    args = parser.parse_args()
    modify_env(args.environs)


if __name__ == "__main__":
    main()
