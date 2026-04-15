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
        if head == None:
            return None
        revers_head = None
        pointer = head
        list_length = 0
        while pointer != None:
            list_length += 1
            revers_head = ListNode(pointer,revers_head)
            pointer = pointer.next
        if list_length < n:
            return head
        elif list_length == n:
            return head.next
        i = 0
        while i < n:
            revers_head = revers_head.next
            if revers_head == None:
                print('Shouldnt get here')
                break
            i += 1
        revers_head.val.next = revers_head.val.next.next
        return head

l = [1]
head = ListNode().list_to_ListNode(l)
sol = Solution()
new_head = sol.removeNthFromEnd(head,1)
print(new_head)