package main

import (
	"fmt"
	"sort"
)
/*=======================================
* @FileName: 18.四数之和.go
* @Description: 计算和 target 相等的不重复四元数组
* @Author: TonyLaw
* @Date: 2021-08-23 01:25:41 Monday
* @Copyright:  © 2021 TonyLaw. All rights reserved.
=========================================*/



func main() {
	var i1 = []int{1, 0, -1, 0, -2, 2}
	var i2 = 0
	fourSum(i1, i2)
	fmt.Println(fourSum(i1, i2))
}
