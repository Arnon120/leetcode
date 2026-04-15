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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1, l2 = l2, l1
        head = l2
        # assumption:
        # l2.val <= l1.val
        while l2 != None:
            if l2.next == None:
                l2.next = l1
                return head
            elif l2.next.val <= l1.val:
                l2 = l2.next
            else: # l2.next.val > l1.val
                temp = l2.next
                l2.next = l1
                l1, l2 = temp, l1

sol = Solution()
nums = [1,2,3,4,5]
nums_2 = [7,8,9]
lisnked_list_1 = ListNode().list_to_ListNode(nums)
lisnked_list_2 = ListNode().list_to_ListNode(nums_2)

l_3 = sol.mergeTwoLists(lisnked_list_1,lisnked_list_2)
