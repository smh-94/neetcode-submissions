# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead


        #                H/NH LN 12
        # 0 -> 1 -> 2 -> (3) ->

        #                  H/NH LN 15
        # 0 -> 1 -> 2 -> (3) -/>

        #           H       NH
        # 0 -> 1 -> (2) <->* 3
        #            H          LN 15
        # 0 -> 1 -> (2) <-* 3

