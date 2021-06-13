# 25. K 个一组翻转链表
# 给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
#
# k是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 进阶：
#
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 示例 2：
#
#
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 示例 3：
#
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
# 示例 4：
#
# 输入：head = [1], k = 1
# 输出：[1]
# 提示：
#
# 列表中节点的数量在范围 sz 内
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
#
#
from typing import List


class ListNode:

    def __init__(self, val):
        if isinstance(val, int) or isinstance(val, str):
            self.val = val
            # 自身尾巴的next就是None
            self.next = None
        elif isinstance(val, List):
            self.val = val[0]
            # 自身尾巴的next就是None
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next

    # 翻转一个子链表， 并且返回新的头和尾
    @staticmethod
    def reverse(head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head


if __name__ == '__main__':
    ln1: ListNode = ListNode([1, 2, 3, 4, 5])
    i1: int = 2
    instance = Solution()
    func = instance.reverseKGroup(ln1, i1)
    print(func)
