# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1, list2):
        res = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next 
            else:
                node.next = list2
                list2 = list2.next 
            node = node.next
        node.next = list1 or list2 
        return res.next 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
        
        res = None 
        for l in lists:
            res = self.mergeTwoLists(res, l)

        return res
        
