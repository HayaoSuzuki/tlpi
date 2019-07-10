import argparse
import os
import sys


def copy_file(src, dst):
    with open(src, "rb") as src_f, open(dst, "wb") as dst_f:
        read_bytes = src_f.read()
        try:
            dst_f.write(read_bytes)
        except OSError:
            print("could not write whole buffer.")
            return os.EX_IOERR
    return os.EX_OK


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    parser.add_argument("target_file")
    args = parser.parse_args()
    ret_code = copy_file(args.source_file, args.target_file)
    sys.exit(ret_code)


if __name__ == "__main__":
    main()
