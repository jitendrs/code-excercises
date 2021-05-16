/*
Go program from The go programming language book page: 77
Program: constant generator iota
Description: const generator iota used to create sequence of related values with spelling out each explicitly.
*/

package main

import "fmt"

type Weekday int

const (
	Sunday Weekday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
)

func main() {
	// auto generated number assign to constant values
	fmt.Println(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)

}
