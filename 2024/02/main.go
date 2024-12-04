package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getData() ([][]int, error) {
	var data [][]int

	file, err := os.Open(os.Args[1])
	if err != nil {
		return nil, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		var intData []int
		split := strings.Fields(scanner.Text())
		for _, num := range split {
			n, err := strconv.Atoi(num)
			if err != nil {
				return nil, err
			}
			intData = append(intData, n)
		}
		data = append(data, intData)
	}

	return data, nil
}

func getUnsafe(nums []int) int {
	asc := false
	dec := false

	for i := 1; i < len(nums); i++ {
		if nums[i-1] < nums[i] {
			asc = true
		} else if nums[i-1] > nums[i] {
			dec = true
		} else {
			return i
		}

		if asc && dec {
			return i
		}

		var diff int
		if asc {
			diff = nums[i] - nums[i-1]
		} else {
			diff = nums[i-1] - nums[i]
		}
		if diff < 1 || diff > 3 {
			return i
		}
	}

	return -1
}

func partOne(data [][]int) int {
	res := 0

	for _, item := range data {
		level := getUnsafe(item)

		if level == -1 {
			res++
		}
	}

	return res
}

func main() {
	data, err := getData()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	res := partOne(data)
	fmt.Println(res)
}
