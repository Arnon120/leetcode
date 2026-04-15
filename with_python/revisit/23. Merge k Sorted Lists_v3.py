import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    """
    def __lt__(self, other):
        if other == None:
            return True
        return self.val < other.val
    Out of submition
    """
    def __str__(self):
        return str(self.val)+' -> '+str(self.next)
    def list_to_ListNode(self, l: list):
        if len(l) == 0:
            return None
        else:
            return ListNode(l[0],self.list_to_ListNode(l[1::]))

class list_Node_container:
    def __init__(self, node: ListNode):
        self.node = node
        if node == None:
            self.key = 10**4 +1
        else: # if val != None
            self.key = node.val
    def __lt__(self,other):
        if self.node == None:
            return False
        elif other.node == None:
            return True
        else: 
            return self.key < other.key


class Solution:
    #def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    def mergeKLists(self, lists) -> ListNode:
        new_list = [list_Node_container(node) for node in lists if node != None]
        if new_list == []:
            return None
        heapq.heapify(new_list)
        listbuilder = ListNode()
        head = listbuilder
        while len(new_list) > 0:
            node = heapq.heappop(new_list).node
            listbuilder.next = node
            node = node.next
            if node != None:
                heapq.heappush(new_list,list_Node_container(node))
            listbuilder = listbuilder.next
        head = head.next
        return head

sol = Solution()
l = [[1,4,5],[1,3,4],[2,6],[]]
nums_1 = l[0]
nums_2 = l[1]
nums_3 = l[2]

lists = [ListNode().list_to_ListNode(nums_1),ListNode().list_to_ListNode(nums_2),ListNode().list_to_ListNode(nums_3)]
#lists = []
l_3 = sol.mergeKLists(lists)
print(l_3)



"""

Biggest Peak

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        res = []
        for link in lists:
            while link != None:
                res.append(link.val)
                link = link.next
        res = sorted(res, reverse = True)
        if res == []: return None
        temp = None
        result = ListNode(res[0], temp)
        for j in range(1, len(res)):
            temp = result
            result = ListNode(res[j],temp)
        return result
        

"""


"""

Best time:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        for h in lists:
            while h:
                self.nodes.append(h.val)
                h = h.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

"""



"""
Biggest Peak space:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def mergeList(p1, p2, lists):
            
            head = None
            prev = None
            
            t1, t2 = lists[p1], lists[p2]
            while t1 and t2:
                node = None
                if t1.val < t2.val:
                    node = t1
                    t1 = t1.next
                else:
                    node = t2
                    t2 = t2.next
                if head is None:
                    head = prev = node
                else:
                    prev.next = node
                    prev = node
            
            t = t1 if t1 else t2
            while t:
                if head is None:
                    head = prev = t
                else:
                    prev.next = t
                    prev = t
                t = t.next
            
            lists[p1] = head
        
        
        n = len(lists)
        if n == 0:
            return None
        
        #2
        #0 1 2 3 4 5 6 7 8 9
        #x   x   x   x   x
        #x       x
        #x               x
        #x
        
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                mergeList(i, i+interval, lists)
            interval *= 2
            
        return lists[0]

"""



"""
Best space:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        count = 0
        self.nodes_arr = []
        while count < len(lists):
            while lists[count] != None:
                self.nodes_arr.append(lists[count].val)
                lists[count] = lists[count].next
            count += 1
            
        head = point = ListNode(0)
        for i in sorted(self.nodes_arr):
            point.next = ListNode(i)
            point = point.next
        return head.next


"""