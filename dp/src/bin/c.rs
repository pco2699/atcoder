use proconio::{fastout, input};
use std::cmp;

#[fastout]
fn main() {
    input! {
        v: [(u32, u32, u32)]
    }
    let mut prev_a = v[0].0; let mut prev_b = v[0].1; let mut prev_c = v[0].2;
    let n = v.len();
    for i in 1..n {
        let (a, b, c) = v[i];
        let current_a = cmp::max(a + prev_b, a + prev_c);
        let current_b = cmp::max(b + prev_a, b + prev_c);
        let current_c = cmp::max(c + prev_b, c + prev_a);

        prev_a = current_a;
        prev_b = current_b;
        prev_c = current_c;
    }
    println!("{}", cmp::max(cmp::max(prev_a, prev_b), prev_c));
}