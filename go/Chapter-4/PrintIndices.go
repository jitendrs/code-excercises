/*
Go program to print indices of elements from The go programming language book page:82
*/

package main

import "fmt"

func main() {
	var a [3]int
	for i, v := range a {
		fmt.Printf("%d %d\n", i, v)
	}

}
