package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	var left []string
	var right []string
	res := 0

	// file, err := os.Open("test_input.txt")
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Fields(line)
		left = append(left, split[0])
		right = append(right, split[1])
	}

	slices.Sort(left)
	slices.Sort(right)

	// Part 1
	for i := range len(left) {
		r, err := strconv.Atoi(right[i])
		if err != nil {
			fmt.Println(err)
			return
		}
		l, err := strconv.Atoi(left[i])
		if err != nil {
			fmt.Println(err)
			return
		}
		if r > l {
			res += r - l
		} else {
			res += l - r
		}
	}

	fmt.Println(res)

	// Part 2
	res = 0
	for _, val := range left {
		c := strings.Count(strings.Join(right, " "), val)
		v,err := strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return
		}
		res += v * c
	}
	
	fmt.Println(res)
}
