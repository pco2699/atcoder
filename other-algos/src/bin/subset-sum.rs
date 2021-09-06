// https://algo-method.com/tasks/309
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        a: [u32; n]
    }
    let result = if solve(&m, &a) { "Yes" } else { "No" };
    println!("{}", result);
}

fn solve(w: &usize, v: &Vec<u32>) -> bool {
    let n = v.len();
    let mut dp = vec![vec![false; n+1]; (*w + 1) as usize];

    for i in 0..=n {
        dp[0][i] = true;
    }

    for i in 1..=n {
        let a = v[i-1] as usize;
        for j in 1..=(*w as usize) {
            if j >= a {
                dp[j][i] = dp[j-a][i-1] || dp[j][i-1];
            } else {
                dp[j][i] = dp[j][i-1];
            }
            
        }
        
    }

    dp[(*w as usize)][n]
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solve() {
        assert_eq!(solve(&10, &vec![7, 5, 3]), true);
        assert_eq!(solve(&6, &vec![9, 7]), false);
    }
}