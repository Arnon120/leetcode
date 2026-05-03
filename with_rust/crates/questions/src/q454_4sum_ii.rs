struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn four_sum_count(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>, nums4: Vec<i32>) -> i32 {
        let mut partial_sums: HashMap<i32, i32>  = HashMap::new();
        let mut count = 0;
        
        for &i in &nums1 {
            for &j in &nums2 {
                *partial_sums.entry(i + j).or_insert(0) += 1;
            }
        }

        for &i in &nums3 {
            for &j in &nums4 {
                count += partial_sums.get(& -(i + j)).unwrap_or(&0);
            }
        }

        count
    }
}