// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution;

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut mut_head = head;
        let Some(unwrapped_head) = mut_head.as_mut() else {return mut_head;};
        let last_val = unwrapped_head.val;
        Self::delete_duplicates_inner(unwrapped_head, last_val);
        
        mut_head
    }

    fn delete_duplicates_inner(head: &mut Box<ListNode>, last_val: i32) {
        let Some(next) = head.next.as_mut() else {return;};
        if next.val == last_val {
            head.next = next.next.take();
            Self::delete_duplicates_inner(head, last_val);
        } else {
            Self::delete_duplicates_inner(next, next.val);
        }

    }
    
}