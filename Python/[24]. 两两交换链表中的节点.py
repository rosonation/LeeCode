# 24. 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
#
#
# 进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
#
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead


if __name__ == '__main__':
    ln1: ListNode = ListNode([1, 2, 3, 4])
    instance = Solution()
    func = instance.swapPairs(ln1)
    print(func)
