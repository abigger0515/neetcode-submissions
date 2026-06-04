# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 
        res = node_prev = ListNode(0, head)

        while True:
            # get first k using fast pointer 
            kth = self.getKth(node_prev, k)
            if not kth:
                break 
            node_next = kth.next

            prev, curr = kth.next, node_prev.next 
            while curr != node_next:
                tmp = curr.next 
                curr.next = prev 
                prev = curr 
                curr = tmp 

            # update node_prev 
            tmp = node_prev.next
            node_prev.next = kth 
            node_prev = tmp 

        return res.next


    def getKth(self, node, k):
        while node and k > 0:
            node = node.next 
            k -= 1

        return node

