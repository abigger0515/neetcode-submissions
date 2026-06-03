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
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None 
                merged_lists.append(self.mergeTwoLists(list1, list2))
            lists = merged_lists 
        return lists[0]

        