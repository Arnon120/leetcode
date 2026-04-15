# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers_remember_the_one(self,l1: ListNode, l2: ListNode,remember: int) -> ListNode:
        if l1 == None:
            if remember == 0:
                return l2
            elif l2 == None:
                return ListNode(1,None)
            else:
                addition = l2.val + remember
                return ListNode(addition % 10, self.addTwoNumbers_remember_the_one(l2.next, None, addition // 10))
        elif l2 == None:
            if remember == 0:
                return l1
            else:
                addition = l1.val + remember
                return ListNode(addition % 10, self.addTwoNumbers_remember_the_one(l1.next, None, addition // 10))
        else:
            addition = l1.val + l2.val + remember
            return ListNode(addition % 10, self.addTwoNumbers_remember_the_one(l1.next, l2.next, addition // 10))
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNumbers_remember_the_one(l1, l2 ,0)



Sol = Solution()



def list_to_ListNode(l: list) -> ListNode:
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return ListNode(l[0])
    else:
        return ListNode(l[0], list_to_ListNode(l[1::]))


"""
l1 = [2,4,3]
l2 = [5,6,4]

l1 = [0]
l2 = [0]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

"""
l1 = [9,9,9,8,8,7,6,5]
l2 = [3]


Node = Sol.addTwoNumbers(list_to_ListNode(l1),list_to_ListNode(l2)) 
print(Node)
