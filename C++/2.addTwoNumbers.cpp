//
//  2.addTwoNumbers.cpp
//  test
//
//  Created by Tony on 2021/6/15.
//
// 2. 两数相加
/* 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
 
 请你将两个数相加，并以相同形式返回一个表示和的链表。

 你可以假设除了数字 0 之外，这两个数都不会以 0开头。



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

*/
#include "2.addTwoNumbers.hpp"
#include <iostream>
#include <nlist.h>
using namespace::std;

//定义结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr, *tail = nullptr;
        int carry = 0;
        while (l1 || l2) {
            int n1 = l1 ? l1->val: 0;
            int n2 = l2 ? l2->val: 0;
            int sum = n1 + n2 + carry;
            if (!head) {
                head = tail = new ListNode(sum % 10);
            } else {
                tail->next = new ListNode(sum % 10);
                tail = tail->next;
            }
            carry = sum / 10;
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        if (carry > 0) {
            tail->next = new ListNode(carry);
        }
        return head;
    }

public:
    ListNode* addListNode(ListNode *pHead, int value) {
        ListNode *pNew = new ListNode(); // 将int的值储存为链表
        pNew->next = nullptr;
        pNew->val = value;
        if (pHead == nullptr) {
            pNew = pHead; //如果是空链表相加，那么新链表就是上面将int转化的链表
        }
        else {
            ListNode *pCopy = pHead; // 拷贝一份链表，作为循环条件
            while (pCopy->next != nullptr) {
                pCopy = pCopy->next; // 指针移动
            }
            pCopy->next = pNew; // 最后指针要指向将int转化的链表，整个pHead链表就移动完了
        }
        return pHead; // 不能返回pCopy，因为它的链表指针移动完了，变成了空
    }
public:
    static ListNode* print(ListNode *printNode) {
        ListNode *p = printNode->next; // ListNode的头为0不要
        while (p != nullptr) {
            cout << p->val << " -> ";
            p = p->next; // 移动指针
        }
        cout << endl;
        return p;
    }
};

int main(int argc, char *argv[]) {
    Solution so;
    ListNode *ln1 = new ListNode();
    ListNode *ln2 = new ListNode();
    so.addListNode(ln1,9);
    so.addListNode(ln1,9);
    so.addListNode(ln1,9);
    so.addListNode(ln1,9);
    so.addListNode(ln1,9);
    so.addListNode(ln1,9);
    so.addListNode(ln1,9);
    so.addListNode(ln2,9);
    so.addListNode(ln2,9);
    so.addListNode(ln2,9);
    so.addListNode(ln2,9);
    so.addTwoNumbers(ln1, ln2);
    so.print(so.addTwoNumbers(ln1, ln2));
    printf("Done.\n");
}
