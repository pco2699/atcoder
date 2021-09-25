use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        v: [usize]
    }
    let sum = v.iter().sum();
    println!("{}", solve(&sum, &v));
}

fn solve(w: &usize, v: &Vec<usize>) -> usize {
    let n = v.len();
    let mut dp = vec![vec![false; n+1]; *w + 1];

    dp[0][0] = true;
    for i in 1..=n {
        let a = v[i-1];
        for j in 0..=*w {
            if j >= a {
                dp[j][i] = dp[j-a][i-1] || dp[j][i-1];
            } else {
                dp[j][i] = dp[j][i-1];
            }
        }
    }

    let mut res = 0usize;
    for j in 0..=*w {
        res += if dp[j][n] { 1 }  else { 0 };
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solve() {
        assert_eq!(solve(&5, &vec![2, 3]), 4);
        assert_eq!(solve(&5, &vec![3, 2]), 4);
        assert_eq!(solve(&10, &vec![2, 3, 5]), 7);
        assert_eq!(solve(&10, &vec![1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 11);
    }
}