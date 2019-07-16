import argparse
import os
import sys
import stat


def tee(file, is_append):
    open_flags = os.O_RDWR | os.O_CREAT
    if is_append:
        open_flags |= os.O_APPEND
    else:
        open_flags |= os.O_TRUNC
    open_mode = (
        stat.S_IRUSR
        | stat.S_IWUSR
        | stat.S_IRGRP
        | stat.S_IWGRP
        | stat.S_IROTH
        | stat.S_IWOTH
    )
    try:
        fd = os.open(file, open_flags, open_mode)
    except FileNotFoundError:
        print(f"No such file: {file}.")
        return os.EX_NOINPUT
    except PermissionError:
        print(f"input {file} can not open.")
        return os.EX_NOPERM
    s = sys.stdin.buffer.read()
    sys.stdout.buffer.write(s)

    try:
        os.write(fd, s)
    except OSError:
        print("cloud not write file.")
        return os.EX_IOERR

    try:
        os.close(fd)
    except OSError:
        print("cloud not close input file.")
        return os.EX_IOERR

    return os.EX_OK


def main():
    parser = argparse.ArgumentParser(
        description="Read from standard input and write to standard output and file."
    )
    parser.add_argument(
        "-a",
        dest="is_append",
        action="store_true",
        help="Append to the given file, do not overwrite.",
    )
    parser.add_argument(
        "file", help="Copy standard input to each file, and also to standard output."
    )
    args = parser.parse_args()
    ret_code = tee(args.file, args.is_append)
    sys.exit(ret_code)


if __name__ == "__main__":
    main()
