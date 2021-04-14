/*
Go program to print the text of each line that appears more than once in the
standard input, preceded by its count, from The go programming language book page:8
Program: FindDupLines
Description: To print text of each line that appears more than once
*/

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	counts := make(map[string]int)
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		counts[input.Text()]++
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}
