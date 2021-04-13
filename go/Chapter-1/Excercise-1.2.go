/*
Go program from The go programming language book page:6
Program: Excercise 1.1
Description: Echo Program to print the index and value of each of its arguments one per line.
*/

package main

import (
	"fmt"
	"os"
)

func main() {

	for index, args := range os.Args[1:] {
		fmt.Println(index, ":", args)
	}
}


