/*=======================================
* @FileName: 4.寻找两个正序数组的中位数.go
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-23 21:54:07 Thursday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
				(题目难度：困难)
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
package main

import (
	"fmt"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	totalLength := Len(nums1) + Len(nums2)
	if totalLength % 2 == 1 {
		midIndex := totalLength / 2
		 else {
		midIndex1, midIndex2 := totalLength / 2 - 1, totalLength / 2
		return float64(getKthElement(nums1, nums2, midIndex1 + 1) + getKthElement(nums1, nums2, midIndex2 + 1)) / 2.0
	}
	return 0
}

func getKthElement(nums1 []int, nums2 []int, k int) int {
	
}