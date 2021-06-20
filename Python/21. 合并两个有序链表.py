# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
# 提示：
#
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列

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
    def mergeTwoLists(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        if ln1 is None:
            return ln2
        elif ln2 is None:
            return ln1
        elif ln1.val < ln2.val:
            ln1.next = self.mergeTwoLists(ln1.next, ln2)
            return ln1
        else:
            ln2.next = self.mergeTwoLists(ln2.next, ln1)
            return ln2


if __name__ == '__main__':
    l1: ListNode = ListNode([1, 2, 4])
    l2: ListNode = ListNode([1, 3, 4])
    instance = Solution()
    func = instance.mergeTwoLists(l1, l2)
    print(func)
