#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let sum: i32 = nums.iter().sum();
        let f_0: i32 =
            nums.iter().enumerate().map(|(index, val)| i32::try_from(index).unwrap() * val).sum();

        let mut current_max = f_0;
        let mut current_f_i = f_0;

        for i in 1..=n - 1 {
            current_f_i = current_f_i + sum - (i32::try_from(n).unwrap() * nums[n - i]);
            current_max = current_max.max(current_f_i);
        }

        current_max
    }

#[allow(dead_code)]
    fn rejected_max_rotate_function(nums: Vec<i32>) -> i32 {
        let mut max_so_far = i32::MIN;
        let n = nums.len();

        for rotation_offset in 0..n {
            let current_max: i32 = nums
                .iter()
                .enumerate()
                .map(|(index, val)| i32::try_from((index + rotation_offset) % n).unwrap() * val)
                .sum();
            println!("current_max: {current_max}");
            max_so_far = max_so_far.max(current_max)
        }

        max_so_far
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(vec![100])]
    #[case(vec![4,3,2,6])]
    fn test_max_rotate_function(#[case] nums: Vec<i32>) {
        let sol = Solution::max_rotate_function(nums.clone());
        let sol_2 = Solution::rejected_max_rotate_function(nums);

        assert_eq!(sol, sol_2)
    }
}
