/*
Description: Go program to prints and count the text of lines that appear more than once in the input using io/ioutil.
			 It reads from stdin or from a list of named files from The go programming language book page:10
*/

package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	counts := make(map[string]int)
	for _, filename := range os.Args[1:] {
		data, err := ioutil.ReadFile(filename)
		if err != nil {
			fmt.Fprintf(os.Stderr, "dup3: %v\n", err)
			continue
		}
		for _, line := range string.Split(string(data), "\n") {
			counts[line]++
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Print("%d\t%s\n", n, line)
		}
	}
}
