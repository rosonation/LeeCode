package com;

import java.util.ArrayList;
import java.util.List;

class Solution6 {
    public static String convert(String s, int numRows) {

        if (numRows == 1) return s;

        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < Math.min(numRows, s.length()); i++)
            rows.add(new StringBuilder());  // 创建空的地址
        // return rows.toString(); [, , ]
        int curRow = 0;
        boolean goingDown = false;

        for (char c : s.toCharArray()) {
            rows.get(curRow).append(c);
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }
        // return rows.toString();  // 是个List<StringBuilder> [PAHN, APLSIIG, YIR]
        StringBuilder ret = new StringBuilder();
        for (StringBuilder row : rows) ret.append(row);
        return ret.toString();
    }

    public static void main(String[] args) {
        String s1 = "PAYPALISHIRING";
        int n1 = 3;
        String result = Solution6.convert(s1, n1);
        System.out.println(result);
    }
}
