# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def list_to_ListNode(self, l: list):
        if len(l) == 0:
            return None
        else:
            return ListNode(l[0],self.list_to_ListNode(l[1::]))
    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        revers_head = None
        pointer = head
        while pointer != None:
            revers_head = ListNode(pointer,revers_head)

sol = Solution()
nums = [1,2,3,4,5]
lisnked_list = ListNode.list_to_ListNode(nums)
