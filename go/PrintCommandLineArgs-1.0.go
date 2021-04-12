/*
Go program to print command line arguments from The go programming language book page:4
Program: PrintCommandLineArgs
Description: To print command line arguments
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	var s, sep string
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s)
}
