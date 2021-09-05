/*=======================================
* @FileName: [1].两数之和.cs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-04 13:56:33 Saturday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
                (题目难度：中等)
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

=========================================*/
using System;
using System.Collections.Generic;

namespace LeetCode
{
    public class Program
    {
        static void Main(String[] args)
        {
            int[] i1 = { 2, 7, 11, 15 };
            int i2 = 9;
            var result = Solution.TwoSum(i1, i2);
            Console.Write("[");
            for (int i = 0; i < result.Length; ++i){
                
                if (i == result.Length - 1)
                {
                    Console.Write(result[i]);
                } else {
                    Console.Write(result[i] + ", ");
                }
            }
            Console.WriteLine("]");
        }
    }
}


public class Solution
{
    public static int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> kvs = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; ++i)
        {
            int complement = target - nums[i];
            if (kvs.ContainsKey(complement) && kvs[complement] != i)
            {
                var ret = new int[] { i, kvs[complement] };
                return ret;
            }
            // 需要对重复值进行判断，若结果包含了重复值，则已经被上面给return了；所以此处对于重复值已经忽略
            if (!kvs.ContainsKey(nums[i]))
            { // 只添加不重复的
                kvs.Add(nums[i], i);
            }
        }
        return new int[] { 0, 0 };  // 空的int[]
    }
}