use std::fs::File;
use std::io::{self, prelude::*, BufReader};


fn main() {
    // to make this work i had to do the return io::Result thing. i will look into this later of
    // how to properly do it
    let file = File::open("./input.txt").expect("something");
    let reader = BufReader::new(file);
    let mut invalidCheck = 0;

    for line in reader.lines() {
        invalidCheck += checkValidLine(line.unwrap());
        println!("{}", invalidCheck);
    }

    println!("{} valid pwds", invalidCheck);

}


fn checkValidLine(input: String) -> i32 {

    let strings = input.split(" ").collect::<Vec<&str>>();
    let mut count = 0;
    let maxMinString = strings[0].split("-").collect::<Vec<&str>>();
    let min = maxMinString[0].parse::<u32>().unwrap() -1;
    let max = maxMinString[1].parse::<u32>().unwrap() -1;
    
    let chr = strings[1].chars().nth(0).unwrap();
    
    let chars = strings[2].chars().collect::<Vec<char>>();
    if (chars.len() < max as usize) || (chars.len() < min as usize) {
        return 0;
    }
    if (chars[min as usize] == chr && chars[max as usize] != chr) || (chars[min as usize] != chr && chars[max as usize] == chr) {
        return 1;
    }
    return 0;
//    for c in strings[2].chars() {
//        if c == chr {
//            count+=1;
//            if count > max {
//                 println!("too high {}", input);
//                 return 0;
//             }
//        }
//    }
//    if count < min {
//        println!("too low: {}", input);
//        return 0;
//    }
//
//    return 1;
}
