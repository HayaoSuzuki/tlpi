import fcntl
import io
import os


def dup(old_io: io.IOBase):
    try:
        new_fd = fcntl.fcntl(old_io, fcntl.F_DUPFD)
    except OSError:
        print("cloud not duplicate file descripter.")
        return os.EX_IOERR
    return new_fd


def main():
    out_f = open("test_dup.txt", "w")
    new_fd = dup(out_f)
    access_mode = fcntl.fcntl(new_fd, fcntl.F_GETFL) & os.O_ACCMODE
    new_fd_readable = access_mode == os.O_RDONLY or access_mode == os.O_RDWR
    new_fd_writeable = access_mode == os.O_WRONLY or access_mode == os.O_RDWR

    print(f"old fd: {out_f.fileno()}")
    print(f"new fd: {new_fd}")

    print(f"old fd readable?: {out_f.readable()}")
    print(f"new fd is readable?: {new_fd_readable}")

    print(f"old fd is writable?: {out_f.writable()}")
    print(f"new fd is writable?: {new_fd_writeable}")

    print(f"old fd flags: {fcntl.fcntl(out_f, fcntl.F_GETFD)}")
    print(f"new fd flags: {fcntl.fcntl(new_fd, fcntl.F_GETFD)}")

    print(f"old open file description: {fcntl.fcntl(out_f, fcntl.F_GETFL)}")
    print(f"new open file description: {fcntl.fcntl(new_fd, fcntl.F_GETFL)}")

    print(f"old current seek position: {os.lseek(out_f.fileno(), 0, os.SEEK_CUR)}")
    print(f"new current seek position: {os.lseek(new_fd, 0, os.SEEK_CUR)}")

    print(f"new current seek move: {os.lseek(new_fd, 10, os.SEEK_CUR)}")
    print(f"old current seek position: {os.lseek(out_f.fileno(), 0, os.SEEK_CUR)}")
    print(f"new current seek position: {os.lseek(new_fd, 0, os.SEEK_CUR)}")

    out_f.close()
    os.close(new_fd)


if __name__ == "__main__":
    main()
