// Exampe to create variable with new()

package main

import "fmt"

func main() {
	p := new(int)
	fmt.Println(*p)
	*p = 2
	fmt.Println(*p)

	fmt.Println("--------------------------------------")
	fmt.Println(*newInt())
}

func newInt() *int {
	return new(int)
}
