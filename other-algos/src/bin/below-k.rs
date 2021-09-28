// アルゴリズムとデータ構造 章末問題5-4参照

fn main() {
    let m = 6;
    let k = 1;
    let a = vec![3, 3, 6];
    let result = if solve(&m, &k, &a) { "Yes" } else { "No" };
    println!("{}", result);
}

fn solve(w: &usize, k: &u32, v: &Vec<u32>) -> bool {
    let n = v.len();
    let mut dp = vec![vec![u32::MAX - 1; n+1]; (*w + 1) as usize];
    dp[0][0] = 0;

    for i in 1..=n {
        let a = v[i-1] as usize;
        for j in 0..=(*w as usize) {
            if j >= a {
                dp[j][i] = std::cmp::min(dp[j-a][i-1] + 1, dp[j][i-1]);
            } else {
                dp[j][i] = dp[j][i-1];
            }
        }
    }

    if dp[(*w as usize)][n] <= *k { true } else { false }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solve() {
        assert_eq!(solve(&5, &2, &vec![2, 3]), true);
        assert_eq!(solve(&6, &1, &vec![3, 3, 6]), true);
    }
}