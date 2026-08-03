# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        temp1 = head
        if temp1.next:
            temp1 = self.reverseList(temp1.next)
            head.next.next = head
        head.next = None

        return temp1
        

            
        