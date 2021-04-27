/*
Example of Tuple assignment which allows several variable to be assign at once.
*/

package main

import "fmt"

// example of swaping variable values
func swap(x, y int) {

	fmt.Printf("Before swaping value of x:%d and value of y:%d\n", x, y)
	x, y = y, x
	fmt.Printf("After swaping value of x:%d and value of y:%d\n", x, y)
}

// calculating gcd of number with swaping of number
func gcd(x, y int) int {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

//n-th Finonacci series
func fib(n int) int {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		x, y = y, x+y
	}
	return x
}

func main() {
	swap(5, 3)
	fmt.Printf("GCD Of Number: %d\n", gcd(423, 53))
	fmt.Println("Fibbonacci Series")
	fmt.Println(fib(5))
}
