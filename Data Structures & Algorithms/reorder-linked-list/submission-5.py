# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        reversing = self.helper(second)

        temp1 = head
        while reversing:
            temp2 = temp1.next
            temp3 = reversing.next
            temp1.next = reversing
            temp1.next.next = temp2
            reversing = temp3
            temp1 = temp2
        return None


    def helper(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        temp1 = head

        if temp1.next:
            temp1 = self.helper(temp1.next)
            head.next.next = head
        
        head.next = None
        return temp1
        
