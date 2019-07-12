import os
import sys
import stat
import typing


def _seek(fd: int, param):
    try:
        offset = int(param)
        os.lseek(fd, offset, os.SEEK_SET)
    except OSError:
        print("cloud not seek file.")
        return os.EX_IOERR
    else:
        print(f"seek {offset} bytes successed.")


def _write(fd: int, param):
    try:
        write_str = param.encode()
        written_bytes_len = os.write(fd, write_str)
    except OSError:
        print("cloud not seek file.")
        return os.EX_IOERR
    else:
        print(f"wrote {written_bytes_len} bytes.")


def _read_as_str(fd: int, param):
    length = int(param)
    read_bytes = os.read(fd, length)
    if len(read_bytes) == 0:
        print(f"end-of-file.")
    else:
        print(read_bytes)


def _read_as_hex(fd: int, param):
    length = int(param)
    read_bytes = os.read(fd, length)
    if len(read_bytes) == 0:
        print(f"end-of-file.")
    else:
        print(read_bytes.hex())


def seek_file(file: str, operatons: typing.List[str]):
    try:
        open_flags = os.O_RDWR | os.O_CREAT
        open_mode = (
            stat.S_IRUSR
            | stat.S_IWUSR
            | stat.S_IRGRP
            | stat.S_IWGRP
            | stat.S_IROTH
            | stat.S_IWOTH
        )
        fd = os.open(file, open_flags, open_mode)
    except FileNotFoundError:
        print(f"No such file: {file}.")
        return os.EX_NOINPUT
    except PermissionError:
        print(f"input {file} can not open.")
        return os.EX_NOPERM

    for operatoin in operatons:
        cmd, param = operatoin[0], operatoin[1:]
        cmds = {"s": _seek, "w": _write, "r": _read_as_str, "R": _read_as_hex}
        if cmd not in cmds:
            print(f"Argument must start with [{cmds.keys()}].")
        else:
            cmds[cmd](fd, param)

    try:
        os.close(fd)
    except OSError:
        print("cloud not close input file.")
        return os.EX_IOERR

    return os.EX_OK


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {__file__} file {{r<length>|R<length>|w<string>|s<offset>}}")
        sys.exit(-1)
    f, operatons = sys.argv[1], sys.argv[2:]
    ret_code = seek_file(f, operatons)
    sys.exit(ret_code)


if __name__ == "__main__":
    main()
