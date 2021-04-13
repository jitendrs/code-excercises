/*
Go program to print command line arguments from The go programming language book page:8
Program: PrintCommandLineArgs-3.0
Description: To print command line arguments with for String package with the help of Join as
			 cost effective solution.
*/

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(strings.Join(os.Args[1:], " "))
}
