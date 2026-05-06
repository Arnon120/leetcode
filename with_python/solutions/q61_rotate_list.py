from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def list_to_ListNode(Self, l: list):
        if len(l) == 0:
            return None
        else:
            return ListNode(l[0], Self.list_to_ListNode(l[1::]))
    
    def into_array(self) -> list:
        tail: list = [self.val]
        if self.next is not None:
            tail += self.next.into_array()
        
        return tail


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        
        list_len = 1
        current = head
        
        while current.next is not None:
            list_len += 1
            current = current.next
        
        end = current

        k = k % list_len
        if k == 0:
            return head

        current = head
        for _ in range(list_len - k - 1):
            current = current.next

        new_end = current
        new_head = current.next
        new_end.next = None
        end.next = head
        return new_head


        
    def rotateLeft(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        
        list_len = 0
        prev: Optional[ListNode] = None
        current = head
        
        end: Optional[ListNode] = None # TODO: No need to initialize this...
        k_th_node: Optional[ListNode] = None

        while current is not None:
            if k == 1:
                k_th_node = current
            
            list_len += 1
            prev = current
            current = current.next
            k -= 1
        
        end = prev

        # Set k_th_node...
        if k > 0:
            k = k % list_len
            while current is not None & k > 1:
                current = current.next
            
            k_th_node = current


        assert k_th_node is not None, "k_th_node should either be set in the first iteration or during the modulus computation."    
        
        new_head = k_th_node.next
        if new_head is None:
            # TODO: check that case...
            return head
        
        k_th_node.next = None
        end.next = head
        return new_head

def test_rotate_right_body(input: List[int], k: int, expected_list: List[int]):
    print(f"testing {input=}, with {k=}")
    head = ListNode.list_to_ListNode(input)
    expected= ListNode.list_to_ListNode(expected_list)

    result = Solution().rotateRight(head=head, k = k)
    assert result.into_array() == expected.into_array(), f"unexpected result {result.into_array()}"
        
def test_rotate_right():
    test_cases = [
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], 1, [3, 1, 2]),
        ([1, 2, 3], 2, [2, 3, 1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 4, [3, 1, 2]),
        ([1, 2, 3], 5, [2, 3, 1]),
        ([1, 2, 3], 6, [1, 2, 3]),
        ([1, 2, 3], 7, [3, 1, 2]),
        ([1, 2, 3], 8, [2, 3, 1]),
    ]

    for input, k, expected_list in test_cases:
        test_rotate_right_body(input=input, k=k, expected_list=expected_list)

test_rotate_right()