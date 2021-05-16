/*
Go program from The go programming language book page:75
Program: illustration of string and number conversions with the help of strconv Sprintf etc.
Description:
*/

package main

import (
	"fmt"
	"strconv"
)

func main() {
	x := 123
	y := fmt.Sprintf("%d", x)
	fmt.Println(y, strconv.Itoa(x))

	// FormatInt and FormatUint can be used to format numbers in a different base:
	fmt.Println(strconv.FormatInt(int64(x), 2))

	// verbs %b, %d, %u and %x are more convenient than Format functions.
	s := fmt.Sprintf("x=%b", x)
	fmt.Println(s)
	u := fmt.Sprintf("x=%d", x)
	fmt.Println(u)
	v := fmt.Sprintf("x=%x", x)
	fmt.Println(v)

	// To parse a string representing an integer, using strconv function Atoi or ParseInt or ParseUint
	xx, err1 := strconv.Atoi("123")
	yy, err2 := strconv.ParseInt("123", 10, 64)
	if err1 == nil && err2 == nil {
		fmt.Println(xx, yy)
	}
}
