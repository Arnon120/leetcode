#[allow(dead_code)]

struct Solution;

impl Solution {
    #[allow(dead_code)]

    pub fn my_pow(mut x: f64, mut n: i32) -> f64 {
        let mut aggregator = 1_f64; 
        
        for i in 0..32 {
            x = if i == 0 {
                match n.cmp(&0) {
                    std::cmp::Ordering::Less => 1_f64/x,
                    std::cmp::Ordering::Equal => break,
                    std::cmp::Ordering::Greater => x,
                }
            } else {
                x * x
            };
            if n % 2 == 1 || n % 2 == -1 {
                aggregator = aggregator * x;
            }
            n = n / 2;
            if n == 0 {
                break;
            }
        }

        aggregator
    }
}

#[cfg(test)]
pub mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(2.0, 1, 2.0)]
    #[case(2.0, -1, 0.5)]
    #[case(2.0, 0, 1.0)]
    #[case(2.0, 2, 4.0)]
    #[case(2.0, 3, 8.0)]
    // #[case(1.0000001, 1 << 30, (1_u32 << 31) as f64)]
    fn test_my_pow (#[case] x: f64, #[case] n: i32, #[case] expected: f64) {
        assert_eq!(Solution::my_pow(x, n), expected)
    }
}