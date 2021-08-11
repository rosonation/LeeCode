package com;

final class Solution12 {
    static int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    static String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public static String intToRoman(int num) {
        StringBuilder roman = new StringBuilder();
        for (int i = 0; i < values.length; ++i) {
            int value = values[i];
            String symbol = symbols[i];
            while (num >= value) {
                num -= value;
                roman.append(symbol);
            }
            if (num == 0) {
                break;  // 没有数字可以转罗马数字了
            }
        }
        return roman.toString();
    }

    public static void main(String[] args) {
        int i1 = 3;
        Solution12.intToRoman(i1);
        System.out.println(Solution12.intToRoman(i1));
    }
}
