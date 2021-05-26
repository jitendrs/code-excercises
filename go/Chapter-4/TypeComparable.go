/*
Go program to for array element type comparable from The go programming language book page:83
*/

package main

import "fmt"

func main() {

	a := [2]int{1, 2}
	b := [...]int{1, 2}
	c := [2]int{1, 3}
	fmt.Println(a == b, a == c, b == c)
	d := [3]int{1, 2}
	fmt.Println(a == d)
}
