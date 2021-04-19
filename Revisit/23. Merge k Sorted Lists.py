import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        if other == None:
            return True
        return self.val < other.val
    """
    Out of submition
    """
    def __str__(self):
        return str(self.val)+' -> '+str(self.next)
    def list_to_ListNode(self, l: list):
        if len(l) == 0:
            return None
        else:
            return ListNode(l[0],self.list_to_ListNode(l[1::]))

class Solution:
    #def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    def mergeKLists(self, lists) -> ListNode:
        heapq.heapify(lists)
        listbuilder = ListNode()
        head = listbuilder
        while len(lists) > 0 and lists[0] != None:
            node = heapq.heappop(lists)
            listbuilder.next = node
            node = node.next
            if node != None:
                heapq.heappush(lists,node)
            listbuilder = listbuilder.next
        head = head.next
        return head

sol = Solution()
l = [[1,4,5],[1,3,4],[2,6],[]]
nums_1 = l[0]
nums_2 = l[1]
nums_3 = l[2]

#lists = [ListNode().list_to_ListNode(nums_1),ListNode().list_to_ListNode(nums_2),ListNode().list_to_ListNode(nums_3)]
lists = [None]
l_3 = sol.mergeKLists(lists)
print(l_3)