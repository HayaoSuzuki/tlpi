import argparse
import os
import stat
import sys

BUF_SIZE = 1024


def copy_file(src, dst):
    try:
        src_fd = os.open(src, os.O_RDONLY)
    except FileNotFoundError:
        print(f"No such file: {src}.")
        return os.EX_NOINPUT
    except PermissionError:
        print(f"input {src} can not open.")
        return os.EX_NOPERM

    dst_flag = os.O_CREAT | os.O_WRONLY | os.O_TRUNC
    dst_mode = (
        stat.S_IRUSR
        | stat.S_IWUSR
        | stat.S_IRGRP
        | stat.S_IWGRP
        | stat.S_IROTH
        | stat.S_IWOTH
    )
    try:
        dst_fd = os.open(dst, dst_flag, dst_mode)
    except OSError:
        print(f"output {dst} can not open.")
        return os.EX_CANTCREAT

    while True:
        read_bytes = os.read(src_fd, BUF_SIZE)
        if len(read_bytes) == 0:
            break
        written_bytes_len = os.write(dst_fd, read_bytes)
        if len(read_bytes) != written_bytes_len:
            print("could not write whole buffer.")
            return os.EX_IOERR
    try:
        os.close(src_fd)
    except OSError:
        print("cloud not close input file.")
        return os.EX_IOERR
    try:
        os.close(dst_fd)
    except OSError:
        print("cloud not close output file.")
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
