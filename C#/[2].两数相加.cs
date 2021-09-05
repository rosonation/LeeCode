/*=======================================
* @FileName: [2].两数相加.cs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-05 13:15:21 Sunday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
                (题目难度：中等)
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零


=========================================*/
using System;

namespace LeetCode
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int x) { val = x; }
    }

    public class Solution
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2) 
        {
            int val = 0;
            ListNode prenode = new ListNode(0);
            ListNode lastnode = prenode;  // 定义空ListNode
            while (l1 != null || l2 != null || val != 0)
            {
                val = val + (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val);
                lastnode.next = new ListNode(val % 10); // 看相加的两个ListNode之和 与 10 取模，两数之和在 0-9 的就保留原来的数字，10-18 就保留个位数字
                lastnode = lastnode.next; // 向后移动指针
                val = val / 10; // 计算两数之和的进位多少（0和1），比如0-9 为0， 10-18 为 1
                l1 = l1 == null ? null : l1.next; // 如果l1是 null，那l1 就结束了，如果不为null就继续遍历 ListNode
                l2 = l2 == null ? null : l2.next; // 如果l2 是 null， 那l2 就结束了， 如果不为 null 就继续遍历 ListNode
            }
            return prenode.next; // 因为prenode是空节点，所以空姐点的 next才是真正的 ListNode 链表
        }
    }

    class Test
    {
        static ListNode generateListNode(int[] vals)
        {
            ListNode res = null;
            ListNode last = null;
            foreach (var val in vals)
            {
                if (res == null) // 没有定义的变量一开始就是null
                {
                    res = new ListNode(val);
                    last = res;
                }
                else
                {
                    last.next = new ListNode(val); // 尾插法
                    last = last.next; // 向后移动指针，对后面进行赋值
                }
            }
            return res;
        }

        static void printList(ListNode l)
        {
            Console.Write("[");
            while (l != null)
            {
                Console.Write($"{l.val}, ");
                l = l.next; // 继续向后遍历链表
            }
            Console.WriteLine("]");
        }

        static void Main(string[] args)
        {
            var l1 = generateListNode(new int[] { 1, 5, 7 });
            var l2 = generateListNode(new int[] { 9, 8, 2, 9 });
            printList(l1);
            printList(l2);
            Solution so = new Solution();
            var sum = so.AddTwoNumbers(l1, l2);
            printList(sum);
        }
    }
}