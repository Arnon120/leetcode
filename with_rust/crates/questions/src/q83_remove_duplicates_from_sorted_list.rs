#![allow(dead_code)]

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

struct Solution;

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut mut_head = head;
        let Some(unwrapped_head) = mut_head.as_mut() else {
            return mut_head;
        };
        let last_val = unwrapped_head.val;
        Self::delete_duplicates_inner(unwrapped_head, last_val);
        mut_head
    }

    fn delete_duplicates_inner(head: &mut Box<ListNode>, last_val: i32) {
        let Some(next) = head.next.as_mut() else {
            return;
        };
        if next.val == last_val {
            head.next = next.next.take();
            Self::delete_duplicates_inner(head, last_val);
        } else {
            Self::delete_duplicates_inner(next, next.val);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn to_list(vals: &[i32]) -> Option<Box<ListNode>> {
        vals.iter().rev().fold(None, |next, &val| Some(Box::new(ListNode { val, next })))
    }

    fn to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut result = vec![];
        while let Some(node) = head {
            result.push(node.val);
            head = node.next;
        }
        result
    }

    #[test]
    fn example1() {
        // [1,1,2] -> [1,2]
        let input = to_list(&[1, 1, 2]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(to_vec(output), vec![1, 2]);
    }

    #[test]
    fn example2() {
        // [1,1,2,3,3] -> [1,2,3]
        let input = to_list(&[1, 1, 2, 3, 3]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(to_vec(output), vec![1, 2, 3]);
    }

    #[test]
    fn empty_list() {
        assert_eq!(Solution::delete_duplicates(None), None);
    }

    #[test]
    fn no_duplicates() {
        let input = to_list(&[1, 2, 3]);
        let output = Solution::delete_duplicates(input);
        assert_eq!(to_vec(output), vec![1, 2, 3]);
    }
}
