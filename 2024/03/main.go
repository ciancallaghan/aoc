package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func getData() ([]string, error) {
	var data []string

	file, err := os.Open(os.Args[1])
	if err != nil {
		return nil, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	return data, nil
}

func partOne(data string) (int, error) {
	res := 0

	s, _ := regexp.Compile(`mul\(\d+,\d+\)`)
	nums := s.FindAllString(data, -1)


	r, _ := regexp.Compile(`\d+`)
	for _, line := range nums {
		var ints []int
		matches := r.FindAllString(line, -1)
		for _, match := range matches {
			n, err := strconv.Atoi(match)
			if err != nil {
				return -1, err
			}
			ints = append(ints, n)
		}

		prod := ints[0]
		for i := 1; i < len(ints); i++ {
			prod = prod * ints[i]
		}
		res += prod
	}
	
	return res, nil
}

func partTwo(data []string) (int, error) {
	res := 0
	r1, _ := regexp.Compile(`do\(\)`)
	r2, _ := regexp.Compile(`don't\(\)`)

	newData := strings.Join(data, "")

	newData = r1.ReplaceAllString(newData, "†")
	newData = r2.ReplaceAllString(newData, "‡")

	var cleanData []rune
	enabled := true
	for _, c := range newData {
		if c == '‡' {
			enabled = false
			continue
		} else if c == '†' {
			enabled = true
			continue
		}

		if enabled {
			cleanData = append(cleanData, c)
		}
	}

	res, err := partOne(string(cleanData))
	if err != nil {
		return -1, err
	}

	return res, nil
}

func main() {
	data, err := getData()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	res, err := partOne(strings.Join(data, ""))
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(res)

	res, err = partTwo(data)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(res)
}
