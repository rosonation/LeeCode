/*=======================================
* @FileName: [4].寻找两个正序数组的中位数.js
* @Description: 
* @Author: TonyLaw
* @Date: 2021-10-10 19:26:57 Sunday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
                (题目难度：中等)
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


=========================================*/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

var findMedianSortedArrays = function (nums1, nums2) {
    let n1 = nums1.length;
    let n2 = nums2.length;

    // 两个数组的总长度
    let len = n1 + n2;

    // 保存当前移动的指针的值（在nums1或nums2移动），和上一个值
    let preValue = -1;
    let curValue = -1;
   
    // 两个指针分别在nums1和nums2上移动
    let point1 = 0;
    let point2 = 0;

    // 需要遍历len / 2 次，当len是奇数时，最后取curValue的值，是偶数时，最后取（preValue + curValue）/ 2的值
    for (let i = 0; i <= Math.floor(len / 2); ++i) {
        preValue = curValue;
        // 需要在nums1上移动point1指针
        if (point1 < n1 && (point2 >= n2 || nums1[point1] < nums2[point2])) {
            curValue = nums1[point1];
            point1++;
        } else {
            curValue = nums2[point2];
            point2++;
        }
    }

    return len % 2 === 0
        ? (preValue + curValue) / 2
        : curValue
};

let n1 = [1, 3]
let n2 = [2]
let result = findMedianSortedArrays(n1, n2)
console.log(result)