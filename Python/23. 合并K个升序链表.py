# 23. 合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
#
# 输入：lists = []
# 输出：[]
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
# 提示：
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        mid = length // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))

    def mergeTwoLists(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        if not ln1 or not ln2:
            return ln1 if ln1 else ln2
        elif ln1.val < ln2.val:
            ln1.next = self.mergeTwoLists(ln1.next, ln2)
            return ln1
        else:
            ln2.next = self.mergeTwoLists(ln2.next, ln1)
            return ln2


if __name__ == '__main__':
    l1: List = [ListNode([1, 4, 5]), ListNode([1, 3, 4]), ListNode([2, 6])]
    instance = Solution()
    func = instance.mergeKLists(l1)
    print(func)
