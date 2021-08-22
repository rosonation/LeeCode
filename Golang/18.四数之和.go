package main

import (
	"fmt"
	"sort"
)

/*=======================================
* @FileName: [18].四数之和.go
* @Description: 找出和target相等的不重复四元数组
* @Author: TonyLaw
* @Date: 2021-08-21 18:22:19 Saturday
=========================================*/

func fourSum(nums []int, target int) (quadruplets [][]int) {
	sort.Ints(nums)
	n := len(nums)
	for i := 0; i < n-3 && nums[i]+nums[i+1]+nums[i+2]+nums[i+3] <= target; i++ {
		if i > 0 && nums[i] == nums[i-1] || nums[i]+nums[n-3]+nums[n-2]+nums[n-1] < target {
			continue
		}
		for j := i + 1; j < n-2 && nums[i]+nums[j]+nums[j+1]+nums[j+2] <= target; j++ {
			if j > i+1 && nums[j] == nums[j-1] || nums[i]+nums[j]+nums[n-2]+nums[n-1] < target {
				continue
			}
			for left, right := j+1, n-1; left < right; {
				if sum := nums[i] + nums[j] + nums[left] + nums[right]; sum == target {
					quadruplets = append(quadruplets, []int{nums[i], nums[j], nums[left], nums[right]})
					for left++; left < right && nums[left] == nums[left-1]; left++ {
					}
					for right--; left < right && nums[right] == nums[right+1]; right-- {
					}
				} else if sum < target {
					left++
				} else {
					right--
				}
			}
		}
	}
	return
}

func main() {
	var i1 = []int{1, 0, -1, 0, -2, 2}
	var i2 = 0
	fourSum(i1, i2)
	fmt.Println(fourSum(i1, i2))
}
