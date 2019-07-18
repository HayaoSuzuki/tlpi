use std::env;

fn main() {
    for (idx, arg) in env::args().enumerate() {
        println!("argv[{}] = {}", idx, arg);
    }
}
