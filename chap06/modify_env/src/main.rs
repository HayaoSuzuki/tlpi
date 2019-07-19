use std::env;

fn modify_env(args: &Vec<String>) {
    for (key, _) in env::vars() {
        env::remove_var(key);
    }

    for arg in args {
        let splited_arg: Vec<_> = arg.split('=').collect();
        let (key, value) = (&splited_arg[0], &splited_arg[1]);
        env::set_var(key, value);
    }

    if env::var("GREET").is_err() {
        env::set_var("GREET", "Hello world");
    }

    if env::var("BYE").is_ok() {
        env::remove_var("BYE");
    }

    for (key, value) in env::vars() {
        println!("{}={}", key, value);
    }
}

fn main() {
    let mut _args = Vec::new();

    for arg in env::args().skip(1) {
        _args.push(arg);
    }
    modify_env(&_args);
}
