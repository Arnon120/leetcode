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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        first_time = True
        def reverse_part(head: ListNode, k: int):
            # return (pointer to this part's head, pointer to next of this part.)
            i = 0
            tail = head
            if tail == None:
                return None,None
            prev = None
            while head != None and i < k:
                i += 1
                following = head.next
                if following == None:
                    print("Do something...")
                head.next = prev
                prev = head
                head = following
            tail.next = head
            return prev,head
        
        while head != None:
            new_head, following = reverse_part(head,k)
            if first_time:
                first_time = False
                ret_val = new_head
            head = following
        return ret_val

sol = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
k = 3
head = ListNode().list_to_ListNode(nums)
new_head = sol.reverseKGroup(head,k)
print(new_head)