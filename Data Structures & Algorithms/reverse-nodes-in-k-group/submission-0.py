# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            groupStart = groupPrev.next

            kth.next = None

            reversedHead = self.reverseLinkedList(groupStart)

            groupPrev.next = reversedHead
            groupStart.next = groupNext

            groupPrev = groupStart


    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev