package main

import (
	"bufio"
	"fmt"
	"os"
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

func partOne(data []string) int {
	res := 0

	for i, line := range data {
		for j, c := range line {
			if c == 'X' {
				if j > 2 &&
					data[i][j-1] == 'M' &&
					data[i][j-2] == 'A' &&
					data[i][j-3] == 'S' {
						res++
				}
				if j < len(line)-3 &&
					data[i][j+1] == 'M' &&
					data[i][j+2] == 'A' &&
					data[i][j+3] == 'S' {
						res++
				}
				if i > 2 &&
					data[i-1][j] == 'M' &&
					data[i-2][j] == 'A' &&
					data[i-3][j] == 'S' {
						res++
				}
				if i < len(data)-3 &&
					data[i+1][j] == 'M' &&
					data[i+2][j] == 'A' &&
					data[i+3][j] == 'S' {
						res++
				}
				if i > 2 &&
					j > 2 &&
					data[i-1][j-1] == 'M' &&
					data[i-2][j-2] == 'A' &&
					data[i-3][j-3] == 'S' {
						res++
				}
				if i > 2 &&
					j < len(line)-3 &&
					data[i-1][j+1] == 'M' &&
					data[i-2][j+2] == 'A' &&
					data[i-3][j+3] == 'S' {
						res++
				}
				if i < len(data)-3 &&
					j > 2 &&
					data[i+1][j-1] == 'M' &&
					data[i+2][j-2] == 'A' &&
					data[i+3][j-3] == 'S' {
						res++
				}
				if i < len(data)-3 &&
					j < len(line)-3 &&
					data[i+1][j+1] == 'M' &&
					data[i+2][j+2] == 'A' &&
					data[i+3][j+3] == 'S' {
						res++
				}
			}
		}
	}

	return res
}

func partTwo(data []string) int {
	res := 0

	for i, line := range data {
		for j, c := range line {
			if c == 'A' &&
				j > 0 &&
				i > 0 &&
				j < len(line)-1 &&
				i < len(data)-1 {
					if data[i-1][j-1] == 'M' &&
						data[i-1][j+1] == 'M' &&
						data[i+1][j-1] == 'S' &&
						data[i+1][j+1] == 'S' {
							res++
					} 
					if data[i-1][j-1] == 'M' &&
						data[i-1][j+1] == 'S' &&
						data[i+1][j-1] == 'M' &&
						data[i+1][j+1] == 'S' {
							res++
					} 
					if data[i-1][j-1] == 'S' &&
						data[i-1][j+1] == 'M' &&
						data[i+1][j-1] == 'S' &&
						data[i+1][j+1] == 'M' {
							res++
					}
					if data[i-1][j-1] == 'S' &&
						data[i-1][j+1] == 'S' &&
						data[i+1][j-1] == 'M' &&
						data[i+1][j+1] == 'M' {
							res++
					}
			}
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
	res = partTwo(data)
	fmt.Println(res)
}
