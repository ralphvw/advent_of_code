package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("data.txt")

	sum := 0

	if err != nil {
		fmt.Println("Error:", err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(fmt.Sprintf("Line: %v", line))
		result := strings.Split(line, "|")
		winningNumbers := strings.Split(result[0], ":")
		winningNumbersArray := strings.Split(winningNumbers[1], " ")
		actualNumbers := result[1]
		actualNumbersArray := strings.Split(actualNumbers, " ")
		fmt.Println(fmt.Sprintf("Winning numbers: %v", winningNumbersArray))
		fmt.Println(fmt.Sprintf("Actual numbers: %v", actualNumbersArray))
		currentSum := 0
		winningSet := map[string]struct{}{}
		for _, v := range winningNumbersArray {
			winningSet[v] = struct{}{}
		}
		for _, v := range actualNumbersArray {
			fmt.Println(currentSum)
			if v == "" {
				continue
			}
			_, exists := winningSet[v]
			if exists {
				if currentSum == 0 {
					currentSum += 1
				} else {
					currentSum *= 2
				}
			}
		}
		sum += currentSum
	}

	fmt.Println(sum)
}
