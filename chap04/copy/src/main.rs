use std::io::Write;

const BUF_SIZE: usize = 8 * 1024;

fn copy<R: ?Sized, W: ?Sized>(reader: &mut R, writer: &mut W) -> std::io::Result<u64>
where
    R: std::io::Read,
    W: std::io::Write,
{
    let mut buf = [0; BUF_SIZE];
    let mut written = 0;
    loop {
        let len = match reader.read(&mut buf) {
            Ok(0) => return Ok(written),
            Ok(len) => len,
            Err(ref e) if e.kind() == std::io::ErrorKind::Interrupted => continue,
            Err(e) => return Err(e),
        };
        writer.write_all(&buf[..len])?;
        written += len as u64;
    }
}

fn main() -> std::io::Result<()> {
    let mut _args = Vec::new();

    for arg in std::env::args().skip(1) {
        _args.push(arg);
    }

    if _args.len() != 2 {
        writeln!(std::io::stderr(), "Usage: copy source_file target_file").unwrap();
    } else {
        // let source_file_path = Path::new(&_args[0]);
        // let target_file_path = Path::new(&_args[1]);
        // std::fs::copy(source_file_path, target_file_path)?;
        let mut source_file = std::fs::File::open(&_args[0])?;
        let mut target_file = std::fs::File::create(&_args[1])?;
        copy(&mut source_file, &mut target_file)?;
    }

    Ok(())
}
