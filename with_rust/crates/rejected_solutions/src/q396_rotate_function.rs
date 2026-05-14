struct Solution;

impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let mut max_so_far = i32::MIN;
        let n = nums.len();

        for rotation_offset in 0..n {
            let current_max: i32 = nums
                .iter()
                .enumerate()
                .map(|(index, val)| i32::try_from((index + rotation_offset) % n).unwrap() * val)
                .sum();
            max_so_far = max_so_far.max(current_max)
        }

        max_so_far
    }
}
