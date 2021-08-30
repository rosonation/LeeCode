/*=======================================
* @FileName: [2].两数相加.swift
* @Description: 
* @Author: TonyLaw
* @Date: 2021-08-26 23:54:02 Thursday
* @Copyright:  © 2021 TonyLaw. All rights reserved.
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

// Definition for single-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil;}
    public init(_ val: Int) {self.val = val; self.next = nil;}
    public init(_ val: Int, _ next: ListNode?) {self.val = val; self.next = next;}
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {  // ? is Optional
        // 未遍历的表链，初始值为传参
        var listNode1 = l1
        var listNode2 = l2 
        // 进值位（两个数相加大于等于10时，将十位数上的值赋给进位值，并参与下一节点的求和）
        var carry: Int = 0
        // 返回结果链表（初始new 一个ListNode即可， var 为任意值）
        let result: ListNode = ListNode(0)
        // 当前节点
        var currentNode: ListNode = result 

        // 存在未遍历的表链或者进位值 carry 大于0 的场合，继续遍历
        while listNode1 != nil || listNode2 != nil || carry > 0 {
            // 求和
            let sum: Int = (listNode1?.val ?? 0) + (listNode2?.val ?? 0) + carry
            // 更新未遍历的表链
            listNode1 = listNode1?.next
            listNode2 = listNode2?.next
            // 更新进位值
            carry = sum / 10
            // 保存本次遍历的节点
            currentNode.next = ListNode(sum % 10)
            // 更新当前节点
            currentNode = currentNode.next!
        }
        return result.next
    }
}

var l1 = ListNode(2,ListNode(3, ListNode(4)))
var l2 = ListNode(5, ListNode(6, ListNode(4)))
var c: ListNode? = Solution().addTwoNumbers(l1, l2)
print(c)