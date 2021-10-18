use proconio::{fastout, input};
use proconio::marker::Chars;
use std::cmp;

#[fastout]
fn main() {
    input! {
        s: Chars,
        v: Chars,
    }
    println!("{}", solve(&s, &v))

}

fn solve(s: &Vec<char>, v: &Vec<char>) -> String {
    let size_s = s.len();
    let size_v = v.len();

    let mut dp = vec![vec![0; size_s+1]; size_v+1];

    for i in 1..=size_s {
        for j in 1..=size_v {
            if s[i-1] == v[j-1] {
                dp[j][i] = dp[j-1][i-1] + 1
            } else {
                dp[j][i] = cmp::max(dp[j-1][i], dp[j][i-1])
            }
        }
    }

    let mut i = size_s; let mut j = size_v;
    let mut res: Vec<char> = Vec::new();
    while i > 0 && j > 0 {
        if dp[j][i] == dp[j-1][i] {
            j = j - 1;
        } else if dp[j][i] == dp[j][i-1] {
            i = i - 1;
        } else if dp[j][i] == dp[j-1][i-1] + 1 {
            res.push(s[i-1]);
            i = i - 1;
            j = j - 1;
            
        }
    }

    res.into_iter().rev().collect()
}



#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solve() {
        assert_eq!(solve(&to_vec_chars(&"axyb".to_owned()), &to_vec_chars(&"abyxb".to_owned())), "ayb");
        assert_eq!(solve(&to_vec_chars(&"aa".to_owned()), &to_vec_chars(&"xayaz".to_owned())), "aa");
        assert_eq!(solve(&to_vec_chars(&"a".to_owned()), &to_vec_chars(&"z".to_owned())), "");
    }

    fn to_vec_chars(s: &String) -> Vec<char> {
        return s.chars().collect::<Vec<_>>();
    }
}
