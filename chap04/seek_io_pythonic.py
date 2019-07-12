import io
import os
import sys
import typing


def _seek(f: io.IOBase, param: str):
    try:
        offset = int(param)
        f.seek(offset, os.SEEK_SET)
    except OSError:
        print("cloud not seek file.")
        return os.EX_IOERR
    else:
        print(f"seek {offset} bytes successed.")


def _write(f: io.IOBase, param: str):
    try:
        write_str = param.encode()
        written_bytes_len = f.write(write_str)
    except OSError:
        print("cloud not seek file.")
        return os.EX_IOERR
    else:
        print(f"wrote {written_bytes_len} bytes.")


def _read_as_str(f: io.IOBase, param: str):
    length = int(param)
    read_bytes = f.read(length)
    if len(read_bytes) == 0:
        print(f"end-of-file.")
    else:
        print(read_bytes)


def _read_as_hex(f: io.IOBase, param: str):
    length = int(param)
    read_bytes = f.read(length)
    if len(read_bytes) == 0:
        print(f"end-of-file.")
    else:
        print(read_bytes.hex())


def seek_file(file: str, operatons: typing.List[str]):
    cmds = {"s": _seek, "w": _write, "r": _read_as_str, "R": _read_as_hex}
    try:
        with open(file, "r+b") as f:
            for operatoin in operatons:
                cmd, param = operatoin[0], operatoin[1:]
                if cmd not in cmds:
                    print("Argument must start with [swrR]")
                else:
                    cmds[cmd](f, param)
    except FileNotFoundError:
        print(f"No such file: {file}.")
        return os.EX_NOINPUT
    except PermissionError:
        print(f"input {file} can not open.")
        return os.EX_NOPERM
    else:
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
