# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。
#
# 进阶：你能尝试使用一趟扫描实现吗？
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
# 提示：
#
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Definition for singly-linked list.
from typing import List


class ListNode:

    def __init__(self, val):
        if isinstance(val, int):
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
    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        def getLength(head1: ListNode) -> int:
            length1 = 0
            while head1:
                length1 += 1
                head1 = head1.next
            return length1

        # same as dummy = ListNode(0, head)
        dummy = ListNode(0)
        dummy.next = head
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


if __name__ == '__main__':
    l1: ListNode = ListNode([1, 2, 3, 4, 5])
    n1: int = 2
    instance = Solution()
    func = instance.removeNthFromEnd(l1, n1)
    print(func)
