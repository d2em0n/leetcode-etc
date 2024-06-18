using System.Collections.Generic;

namespace LC2
{
    //Definition for singly-linked list.
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
    public class Solution
    {      

        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            var current = new ListNode();
            var addition = 0;
            var answer = current;
            while (l1 != null || l2 != null || addition != 0)
            {
                var result = l1.val + l2.val + addition;
                current.val = result % 10;
                addition = result / 10;
                l1 = l1.next != null ? l1.next : new ListNode();
                l2 = l2.next != null ? l2.next : new ListNode();
                if (l1.val == 0 && l2.val == 0 && l1.next == null && l2.next == null && addition == 0)
                    break;
                current.next = new ListNode();
                current = current.next;
            }
            return answer ;
        }

        public static void Main()
        {
            Console.WriteLine("main");
        }
    }
}
