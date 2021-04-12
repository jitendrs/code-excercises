/*
Go program to print command line arguments from The go programming language book page:6
Program: PrintCommandLineArgs
Description: To print command line arguments with for loop condtional functionality
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	s, sep := "", ""
	for _, arg := range os.Args[1:] {
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}
