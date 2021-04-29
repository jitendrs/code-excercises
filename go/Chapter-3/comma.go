/*
Go program lastindex from The go programming language book page:73
Description: comma inserts commas in a non-negative decimal integer string.
*/
package main

import "fmt"

func comma(s string) string {
	n := len(s)
	if n <= 3 {
		return s
	}
	return comma(s[:n-3]) + "," + s[n-3:]
}

func main() {
	fmt.Println(comma("1434324322345"))
}
