/*
Passing Pointer argument to a function makes it possible for a function to update the variable that was indirectly passed.
This function increments the variable that its argument points to and returns the new value of the variable.
*/

package main

import (
	"fmt"
)

func incr(p *int) int {
	*p++ // increments what p points to;does not change p
	return *p
}

func main() {
	v := 1
	incr(&v)              // side effect: v is now 2
	fmt.Println(incr(&v)) // "3" (and v is 3)
}
