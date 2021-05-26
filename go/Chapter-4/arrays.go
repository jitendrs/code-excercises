/*
Go program to create and print array from The go programming language book page:81
*/

package main

func main() {
	var v [3]int
	println("Print first element of array.", v[0])
	println("Print the last element of array.", v[len(v)-1])
}
