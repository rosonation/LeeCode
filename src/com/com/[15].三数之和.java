package com;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution15 {
    public static List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        // 枚举 a
        for (int first = 0; first < n; ++first) {
            // 需要和上一次枚举的数不相同
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }
            // c 对应的指针初始指向数组的最右端
            int third = n - 1;
            int target = -nums[first]; // 等于secode + third 的相反数
            // 枚举 b
            for (int second = first + 1; second < n; ++second) {
                // 需要和上一次枚举的数不同
                if (second > first + 1 && nums[second] == nums[second - 1]) {
                    continue;
                }
                // 需要保证 b 的指针在 c 的指针的左边
                while (second < third && nums[second] + nums[third] > target) {
                    --third;   // c 的指针的数大了，需要左边减少 b 和 c 的总和
                }
                // 如果指针重合，随着 b 后续的增加
                // 就不就满足 a+b+c=0 并且 b  < c 的 c 了，可以退出循环了
                if (second == third) {
                    break;
                }
                if (nums[second] + nums[third] == target) {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[first]);
                    list.add(nums[second]);
                    list.add(nums[third]);
                    ans.add(list);
                    System.out.println(nums[first]);
//                        + nums[second] + nums[third]);
                }
            }
        }
        return ans;
    }

   public static void main(String[] args) {
       int[] a = {-1, 0, 1, 2, -1, -4};
       for (int i = 0 ; i < a.length; ++i) {
           System.out.println("index is :" + i + ";value is :" + a[i]);
       }
       Solution15.threeSum(a);
   }
}