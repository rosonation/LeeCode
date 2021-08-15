package com;

class Solution14 {
    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        String prefix = strs[0];
        for (String str : strs) {
            prefix = longestCommonPrefix(prefix, str);
            if (prefix.length() == 0) {
                break;
            }
        }
        return prefix;
    }

    public static String longestCommonPrefix(String str1, String str2) {
        int length = Math.min(str1.length(), str2.length());
        int index = 0;
        while (index < length && str1.charAt(index) == str2.charAt(index)) {
            ++index;
        }
        return str1.substring(0, index);
    }

    public static void main(String[] args) {
        String[] s1 = {"flower", "flow", "flight"};
        Solution14.longestCommonPrefix(s1);
        System.out.print(Solution14.longestCommonPrefix(s1));
    }
}
