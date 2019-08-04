package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	nums := insertionSort(scanNums(N), N)
	printNums(nums)
}

func insertionSort(nums []int, n int) []int {
	for i := 1; i < n; i++ {
		printNums(nums)
		v := nums[i]
		var j int
		for j = i - 1; j >= 0 && nums[j] > v; j-- {
			nums[j+1] = nums[j]
		}
		nums[j+1] = v

	}
	return nums
}

func scanNums(len int) (nums []int) {
	var num int
	for i := 0; i < len; i++ {
		fmt.Scan(&num)
		nums = append(nums, num)
	}
	return
}

func printNums(nums []int) {
	for k := 0; k < len(nums)-1; k++ {
		fmt.Printf("%d ", nums[k])
	}
	fmt.Println(nums[len(nums)-1])
}
