# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get the kth node 
        # reverse start ~ kth node 
        # update the start node (now the end of the reversed list) 
            # and kth node (now the start of the reversed list)


        res = prev_node = ListNode(0, head)
        while True:
            kth_node = self.getKthNode(prev_node, k)
            if not kth_node:
                break 
            next_node = kth_node.next
            # reverse 
            prev, curr = kth_node.next, prev_node.next 
            while curr != next_node:
                tmp = curr.next 
                curr.next = prev 
                prev = curr 
                curr = tmp 
            # update prev_node 
            tmp = prev_node.next 
            prev_node.next = kth_node 
            prev_node = tmp 

        return res.next 

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr 