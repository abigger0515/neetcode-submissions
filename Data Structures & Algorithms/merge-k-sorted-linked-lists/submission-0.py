# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None 
        elif len(lists) == 1:
            return lists[0]
        
        list1 = lists[0]
        
        # merge 2 lists 
        for list2 in lists[1:]:
            res = node = ListNode()
            # list2 = lists[1]
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next 
                node = node.next 
            node.next = list1 or list2
            list1 = res.next 

        return list1
        
