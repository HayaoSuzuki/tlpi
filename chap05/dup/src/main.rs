extern crate libc;
extern crate nix;

use libc::O_ACCMODE;
use libc::O_RDONLY;
use libc::O_RDWR;
use libc::O_WRONLY;
use nix::fcntl::fcntl;
use nix::fcntl::FcntlArg::F_DUPFD;
use nix::fcntl::FcntlArg::F_GETFD;
use nix::fcntl::FcntlArg::F_GETFL;
use std::fs::File;
use std::os::unix::io::AsRawFd;
use std::os::unix::io::RawFd;

fn dup(old_fd: &RawFd) -> i32 {
    let new_fd = fcntl(*old_fd, F_DUPFD(*old_fd)).unwrap();
    new_fd
}

fn main() {
    let old_file = File::create("dummy.txt").unwrap();
    let old_fd = old_file.as_raw_fd();
    let new_fd = dup(&old_fd);

    let old_access_mode = fcntl(old_fd, F_GETFL).unwrap() & O_ACCMODE;
    let new_access_mode = fcntl(old_fd, F_GETFL).unwrap() & O_ACCMODE;

    let old_fd_readable = (old_access_mode == O_RDONLY) | (old_access_mode == O_RDWR);
    let new_fd_readable = (new_access_mode == O_RDONLY) | (new_access_mode == O_RDWR);
    let old_fd_writeable = (old_access_mode == O_WRONLY) | (old_access_mode == O_RDWR);
    let new_fd_writeable = (new_access_mode == O_WRONLY) | (new_access_mode == O_RDWR);

    println!("old fd: {}", &old_fd);
    println!("new fd: {}", &new_fd);

    println!("old fd is readable?: {}", old_fd_readable);
    println!("new fd is readable?: {}", new_fd_readable);
    println!("old fd is writable?: {}", old_fd_writeable);
    println!("new fd is writable?: {}", new_fd_writeable);

    println!("old fd flags: {}", fcntl(old_fd, F_GETFD).unwrap());
    println!("new fd flags: {}", fcntl(new_fd, F_GETFD).unwrap());

    println!(
        "old open file description: {}",
        fcntl(old_fd, F_GETFL).unwrap()
    );
    println!(
        "new open file description: {}",
        fcntl(new_fd, F_GETFL).unwrap()
    );
}
