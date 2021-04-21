// Function to return address of local variable. Each call to function returns distict memory address.

package main

import "fmt"

func f() *int {
	v := 1
	return &v
}

func main() {

	var p = f()
	fmt.Println("Address of function return f():", p)
	// Each function call returns a distinct value
	fmt.Println(f() == f())

}
