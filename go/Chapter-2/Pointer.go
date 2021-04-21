// Pointer

package main

import (
	"fmt"
)

func main() {

	x := 1
	p := &x
	fmt.Printf("Address of x is %d\n", &x)
	fmt.Printf("Address of p is %d\n", &p)
	fmt.Printf("pointer is pointing to value: %d\n", *p)
	*p = 2
	fmt.Printf("After changing value of pointer to which it's pointing too. %d\n", *p)
	fmt.Printf("Now value of x is. %d\n", x)

	fmt.Printf("Now address of x is %d\n", &x)
	fmt.Printf("Now address of p is %d\n", &p)
	fmt.Printf("Now pointer is pointing to value: %d\n", *p)

	fmt.Println("\n------------------------------------")
	var xi, yi int
	fmt.Println(&xi == &xi, &xi == &yi, &xi == nil)
	fmt.Printf("Address of xi is %d\n", &xi)
	fmt.Printf("Address of yi is %d\n", &yi)
}
