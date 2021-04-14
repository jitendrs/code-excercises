/*
Description: Go program to prints and count the text of lines that appear more than once in the input.
			 It reads from stdin or from a list of named files from The go programming language book page:10
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Printf(os,Error"")
			}
		}
	}
}

func countLines(f *os.File, counts map[string]int) {

}
