package java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution1 {
    public static int[] twoSum(int[] numbs, int target) {
        Map<Integer, Integer> hashtable = new HashMap<>();
        for (int i = 0; i < numbs.length; ++i) {
            if (hashtable.containsKey(target - numbs[i])) {
                return new int[]{hashtable.get(target - numbs[i]), i};
            }
            hashtable.put(numbs[i], i);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int[] a = {1, 7, 11, 15};
        int b = 8;
        Solution1.twoSum(a, b);
        System.out.println(Arrays.toString(Solution1.twoSum(a, b)));
    }
}