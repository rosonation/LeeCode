package com;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution1 {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashtable = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            if (hashtable.containsKey(target - nums[i])) {
                return new int[]{hashtable.get(target - nums[i]), i};
            }
            hashtable.put(nums[i], i);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int[] a = {1, 7, 11, 15};
        int b = 9;
        Solution1.twoSum(a, b);
        System.out.println(Arrays.toString(Solution1.twoSum(a, b)));
    }
}