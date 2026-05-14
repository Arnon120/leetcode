struct Solution;

fn get_from_array_with_distorted_index(nums: &[i32], index: usize) -> Option<i32> {
    if index == 0 {
        None
    } else {
        Some(nums[index - 1])
    }
}

impl Solution {
    // Go from the end of the arrays to the beggining! Fill the end of nums1 in decending order...
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut i: usize = m.try_into().unwrap();
        let mut j: usize = n.try_into().unwrap();
        let mut k: usize = i + j;
        while k > 0 {
            if get_from_array_with_distorted_index(nums1, i)
                < get_from_array_with_distorted_index(nums2, j)
            {
                nums1[k - 1] = nums2[j - 1];
                j -= 1;
            } else {
                nums1[k - 1] = nums1[i - 1];
                i -= 1;
            }
            k -= 1;
        }
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(vec![0], vec![], vec![0])]
    #[case(vec![], vec![1], vec![1])]
    #[case(vec![0], vec![1], vec![0,1])]
    #[case(vec![1], vec![0], vec![0,1])]
    #[case(vec![1, 3, 5], vec![2, 4, 6], vec![1,2,3,4,5,6])]
    fn test_merge(
        #[case] mut nums1: Vec<i32>,
        #[case] mut nums2: Vec<i32>,
        #[case] expected: Vec<i32>,
    ) {
        let m = nums1.len();
        let n = nums2.len();

        nums1.append(&mut (0..n).map(|_| 0).collect());
        Solution::merge(&mut nums1, m.try_into().unwrap(), &mut nums2, n.try_into().unwrap());
        let copy_of_nums1 = nums1.clone();
        nums1.sort();
        assert_eq!(nums1, copy_of_nums1);

        assert_eq!(nums1, expected);
    }
}
