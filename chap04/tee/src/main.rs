extern crate getopts;

use getopts::Options;
use std::env;
use std::fs::File;
use std::fs::OpenOptions;
use std::io::BufReader;
use std::io::BufWriter;
use std::io::Read;
use std::io::Write;

fn tee(out: &str, is_append: bool) -> std::io::Result<()> {
    let mut output_file;
    if is_append {
        output_file = OpenOptions::new().append(true).open(out)?;
    } else {
        output_file = File::create(out)?;
    };
    let mut bufferd_output_file = BufWriter::new(output_file);

    let stdin = std::io::stdin();
    let mut bufferd_stdin = BufReader::new(stdin.lock());
    let mut stdin_payload = Vec::new();
    bufferd_stdin.read_to_end(&mut stdin_payload)?;

    let stdout = std::io::stdout();
    let mut stdout_buffer = BufWriter::new(stdout.lock());

    stdout_buffer.write(&stdin_payload)?;
    bufferd_output_file.write(&stdin_payload)?;
    Ok(())
}

fn print_usage(program: &str, opts: Options) {
    let brief = format!("Usage: {} [options] FILE", program);
    print!("{}", opts.usage(&brief));
}

fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let program = args[0].clone();

    let mut opts = Options::new();
    opts.optflag("a", "append", "append to the given file, do not overwrite.");
    opts.optflag("h", "help", "print this help menu");
    let matches = match opts.parse(&args[1..]) {
        Ok(m) => m,
        Err(f) => panic!(f.to_string()),
    };
    if matches.opt_present("h") {
        print_usage(&program, opts);
        return Ok(());
    }
    let is_append = matches.opt_present("a");
    let output = if !matches.free.is_empty() {
        matches.free[0].clone()
    } else {
        print_usage(&program, opts);
        return Ok(());
    };
    tee(&output, is_append)?;
    Ok(())
}
