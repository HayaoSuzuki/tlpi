use std::env::args;

fn main() {
    for (idx, arg) in args().into_iter().enumerate() {
        println!("argv[{}] = {}", idx, arg);
    }
}
