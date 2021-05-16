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
        def check_length_less_then_k(head: ListNode, k: int):
            i = 0
            while head != None and i < k:
                i += 1
                head = head.next
            return i == k
        def reverse_part(head: ListNode, k: int):
            # return (pointer to this part's head, pointer to last node of this part.)
            i = 0
            tail = head
            if tail == None:
                return None,None
            if not check_length_less_then_k(head,k):
                return head, None
            prev = None
            while head != None and i < k:
                i += 1
                following = head.next
                #if following == None:
                #    print("Do something...")
                head.next = prev
                prev = head
                head = following
            tail.next = head
            return prev,tail
        
        tail = None
        while head != None:
            new_head, new_tail = reverse_part(head,k)
            if tail != None:
                tail.next = new_head
            if first_time:
                first_time = False
                ret_val = new_head
            if new_tail == None:
                break
            head = new_tail.next
            tail = new_tail
        return ret_val

sol = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
k = 4
head = ListNode().list_to_ListNode(nums)
new_head = sol.reverseKGroup(head,k)
print(new_head)