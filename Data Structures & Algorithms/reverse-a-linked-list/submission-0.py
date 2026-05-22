# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None
        # 1 -> 2 -> 3 -> None 
        while curr:
            tmp = curr.next # 2
            curr.next = prev # 
            prev = curr 
            curr = tmp 

        return prev 
