/*
Go program from The go programming language book page:6
Program: Excercise 1.1
Description: Echo Program to also print os.Args[0], then name of the command that invoked it.
*/

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(os.Args[0], strings.Join(os.Args[1:], " "))
}
