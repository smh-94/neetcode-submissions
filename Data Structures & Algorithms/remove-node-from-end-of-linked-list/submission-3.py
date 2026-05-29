# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        dummy = ListNode(0, head)
        fcount = 0
        scount = 0
        slow = dummy
        fast = dummy
        
        while fast.next and fast.next.next:
            fcount += 2
            scount += 1
            fast = fast.next.next
            slow = slow.next
        
        if fast.next:
            fcount += 1
            fast = fast.next
            
        if scount > (fcount - n):
            slow = dummy
            scount = 0

        while scount < (fcount - n):
            slow = slow.next
            scount += 1

        slow.next = slow.next.next
        return dummy.next