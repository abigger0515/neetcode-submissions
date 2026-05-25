# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle 
        fast, slow = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        # reverse the second half, starts with slow.next 
        second = slow.next 
        slow.next = None  # to cut off the fist half 
        prev = None 
        while second:
            tmp = second.next
            second.next = prev 
            prev = second
            second = tmp

        # merge first and second half 
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2 


