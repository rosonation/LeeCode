/*=======================================
* @FileName: 2两数相加.go
* @Description:
* @Author: TonyLaw
* @Date: 2021-09-05 20:57:02 Sunday
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
package main;

import "fmt"

//Definition for singly-linked list.
type ListNode struct {
	Val int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) (head *ListNode) {
	var tail *ListNode
	carry := 0
	for l1 != nil || l2 != nil || carry != 0{
		n1, n2 := 0, 0
		if l1 != nil {
			n1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			n2 = l2.Val
			l2 = l2.Next
		}
		sum := n1 + n2 + carry
		sum, carry = sum % 10, sum / 10
		if head == nil {   // 一开始head是nil
			head = &ListNode{Val:  sum}
			tail = head
		} else {
			tail.Next = &ListNode{Val: sum}
			tail = tail.Next
		}
	}
	return head
}

func main() {
	l1 := &ListNode{Val: 3}
	l2 := &ListNode{Val: 4}
	l3 := &ListNode{Val: 2}
	l2.Next = l1
	l3.Next = l2
	l4 := &ListNode{Val: 4}
	l5 := &ListNode{Val: 6}
	l6 := &ListNode{Val: 5}
	l5.Next = l4
	l6.Next = l5
	var result = addTwoNumbers(l3, l6)
	fmt.Print("[")
	for result != nil {
		if result.Next != nil {
			fmt.Print(result.Val, ", ")
		} else {
			fmt.Print(result.Val)
		}
		result = result.Next
	}
	fmt.Println("]")
}
