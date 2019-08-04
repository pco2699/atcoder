package main

import "fmt"

func main() {
	var N, Y int
	fmt.Scanf("%d %d", &N, &Y)
	breakFlag := false

	var x, y, z int

	for i := 0; i <= N; i++ {
		for j := 0; j <= N-i; j++ {
			k := N - i - j
			if i*10000+j*5000+k*1000 == Y {
				x = i
				y = j
				z = k
				breakFlag = true
				break
			}
		}
		if breakFlag == true {
			break
		}
	}
	if breakFlag {
		fmt.Printf("%d %d %d\n", x, y, z)
	} else {
		fmt.Println("-1 -1 -1")
	}
}
