use std::env;

fn main() {
    let key = "FOO";
    env::set_var(key, "BAR");
    for (key, value) in env::vars() {
        println!("{}={}", key, value);
    }
}
