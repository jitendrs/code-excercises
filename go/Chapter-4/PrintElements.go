/*
Go program to print elements from The go programming language book page:82
*/

package main

import "fmt"

func main() {
	var v [3]int
	for _, e := range v {
		fmt.Printf("%d\n", e)
	}
	// By default elements values are set to zero below examples shows assignments

	var q [3]int = [3]int{1, 2, 3}
	var r [3]int = [3]int{1, 2}
	fmt.Println("Print last elements from array")
	fmt.Println(r[2])
	fmt.Println("Print all the elements from array")
	fmt.Println(q)
}
