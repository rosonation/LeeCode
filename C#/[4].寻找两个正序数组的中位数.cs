/*=======================================
* @FileName: [4].寻找两个正序数组的中位数.cs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-22 20:53:42 Wednesday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
                (题目难度: 困难)
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
using System;
using System.Collections.Generic;

namespace LeetCode
{
    public class Solution
    {
        public double FindMedianSortedArrays(int[] nums1, int[] nums2)
        {
            int m = nums1.Length;
            int n = nums2.Length;
            int len = m + n;
            var resuleIndex = len / 2;
            List<int> list = new List<int>(nums1);
            list.AddRange(nums2);
            list.Sort();
            if (len % 2 == 0)
            {
                return (list[resuleIndex - 1] + list[resuleIndex]) / 2.0;
            }
            else
            {
                return list[resuleIndex];
            }
        }
        static void Main(string[] args)
        {
            int[] i1 = { 1, 3 };
            int[] i2 = { 2 };
            Solution so = new Solution();
            var target = so.FindMedianSortedArrays(i1, i2);
            Console.WriteLine(target);
        }
    }
}