use std::fs::OpenOptions;
use std::io::Read;
use std::io::Seek;
use std::io::SeekFrom;
use std::io::Write;

fn seek_io(file: &mut std::fs::File, operations: &[String]) -> std::io::Result<()> {
    for operation in operations {
        let cmd = operation.chars().nth(0).unwrap();
        let param = &operation[1..];

        if cmd == 's' {
            let offset: i64 = param.parse().unwrap();
            file.seek(SeekFrom::Current(offset))?;
        } else if cmd == 'w' {
            write!(file, "{}", param)?;
        } else if cmd == 'r' {
            let length: u64 = param.parse().unwrap();
            let mut buf = String::new();
            file.take(length).read_to_string(&mut buf)?;
            println!("{:?}", buf);
        } else if cmd == 'R' {
            let length: u64 = param.parse().unwrap();
            let mut buf = Vec::new();
            file.take(length).read_to_end(&mut buf)?;
            let hex_string = buf.iter().map(|n| format!("{:02X}", n)).collect::<String>();
            println!("{:X?}", hex_string);
        }
    }

    Ok(())
}

fn main() -> std::io::Result<()> {
    let mut _args = Vec::new();

    for arg in std::env::args().skip(1) {
        _args.push(arg);
    }

    if _args.len() < 2 {
        writeln!(
            std::io::stderr(),
            "Usage: seek_io file {{r<length>|R<length>|w<string>|s<offset>}}."
        )
        .unwrap();
    } else {
        let mut file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open(&_args[0])?;
        let operations = &_args[1..];

        seek_io(&mut file, &operations)?;
    }

    Ok(())
}
