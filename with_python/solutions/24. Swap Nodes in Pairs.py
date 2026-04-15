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
    def swapPairs(self, head: ListNode) -> ListNode:
        pointer = head
        while pointer != None:
            if pointer.next == None:
                break
            else:
                temp = pointer.val
                pointer.val = pointer.next.val
                pointer.next.val = temp
            pointer = pointer.next.next

        return head

sol = Solution()
l = []
head = ListNode().list_to_ListNode(l)
new_head = sol.swapPairs(head)
print(new_head)


"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second

"""