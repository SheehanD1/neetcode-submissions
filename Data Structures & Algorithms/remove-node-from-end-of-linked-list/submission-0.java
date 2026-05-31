/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        ListNode temp2 = head;
        int count = 0;

        ListNode counter = head;
        while (counter != null) {
            counter = counter.next;
            count++;
        }

        if (n == count) {
            return head.next;
        }

        int cur = 0;
        while (cur < count - n - 1) {  
            temp2 = temp2.next;
            cur++;
        }

        temp2.next = temp2.next.next;

        return temp;
    }
}

