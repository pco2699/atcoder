// -*- coding:utf-8-unix -*-

use proconio::input;
use std::ops::Add;
use std::fmt;

// ABC086C - Traveling
// https://atcoder.jp/contests/abs/fasks/arc089_a

#[derive(Debug, Copy, Clone, PartialEq, Display)]
struct Point<T> {
    x: T,
    y: T,
}

impl <T: Add<Output = T>>Add for Point<T> {
    type Output = Self;
    fn add(self, other: Self) -> Self {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

impl <T: fmt::Display>fmt::Display for Point<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}




fn main() {
    input! {
        n: usize,
        p0: Point<f64>,
        pn_2: Point<f64>,
    }
    println!("{}", p0 + pn_2);
}
