struct Solution;

impl Solution {
    pub fn get_permutation(n: i32, k: i32) -> String {
        let mut remaining_symbols: Vec<char> = (1..=(n as u8)).map(|i| (i + 48).into()).collect();
        let mut output: Vec<char> = vec![];
        let mut n = n as usize;
        let mut k = k as usize - 1;
        let mut factorial: usize = (1..=n).product();  // Holds n!
        while n > 0 {
            factorial = factorial / n; // Holds (n-1)!
            let offset_of_char = k / factorial;
            output.push(remaining_symbols.remove(offset_of_char));
            k = k % factorial;
            n = n - 1;
        }

        output.into_iter().collect()
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(1, 1, "1")]
    #[case(2, 1, "12")]
    #[case(2, 2, "21")]
    #[case(3, 1, "123")]
    #[case(3, 2, "132")]
    #[case(3, 3, "213")]
    #[case(3, 4, "231")]
    #[case(3, 5, "312")]
    #[case(3, 6, "321")]
    fn test_get_permutation(#[case] n: i32, #[case] k: i32, #[case] expected: &str) {
        assert_eq!(&Solution::get_permutation(n, k), expected)
    }
}