use std::io::Write;
use std::path::Path;

fn main() -> std::io::Result<()> {
    let mut _args = Vec::new();

    for arg in std::env::args().skip(1) {
        _args.push(arg);
    }

    if _args.len() != 2 {
        writeln!(std::io::stderr(), "Usage: copy source_file target_file").unwrap();
        std::process::exit(-1);
    } else {
        let source_file_path = Path::new(&_args[0]);
        let target_file_path = Path::new(&_args[1]);
        std::fs::copy(&source_file_path, &target_file_path)?;
    }

    Ok(())
}
