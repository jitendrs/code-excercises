/*
Go program lastindex from The go programming language book page:72
Description: Get LastIndex of string with strings.LastIndex library function.
*/

package main

import "strings"

func basename(s string) string {
	slash := strings.LastIndex(s, "/")
	s = s[slash+1:]
	if dot := strings.LastIndex(s, "."); dot >= 0 {
		s = s[:dot]
	}
	return s
}

func main() {
	println(basename("Hello/b/c/g/g/y.txt"))
}
