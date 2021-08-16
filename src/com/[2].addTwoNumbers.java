


//import java.util.Arrays;

//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution2 {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = null, tail = null;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int n1 = l1 != null ? l1.val : 0;
            int n2 = l2 != null ? l2.val : 0;
            int sum = n1 + n2 + carry;
            if (head == null) {
                head = tail = new ListNode(sum % 10);
            } else {
                tail.next = new ListNode(sum % 10);
                tail = tail.next;
            }
            carry = sum / 10;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        if (carry > 0) {
            tail.next = new ListNode(carry);
        }
        return head;
    }

    public static void addListNode(ListNode l4, int value) {
        ListNode pNew = new ListNode();
        pNew.next = null;
        pNew.val = value;
        ListNode copy = l4;
        while (copy.next != null) {
            copy = copy.next;
        }
        copy.next = pNew;
    }

    public static void listPrint(ListNode l3) {
        ListNode p = l3;
        while (p != null) {
            System.out.print(p.val + " -> ");
            p = p.next;
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2);
        Solution2.addListNode(l1, 4);
        Solution2.addListNode(l1, 3);
        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
        listPrint(l1);
        Solution2.addTwoNumbers(l1, l2);
        listPrint(Solution2.addTwoNumbers(l1, l2));
    }
}
