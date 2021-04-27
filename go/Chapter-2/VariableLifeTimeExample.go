/* lifetime of variable depenends on the accessiblity of variable. If variable is unreachable which
   mean it can be garbage collected and recycle.
*/

package main

import "fmt"

var global *int

func main() {
	f()
	g()
}

func f() {
	var x int
	x = 1
	global = &x
	fmt.Println(*global)
}

func g() {
	y := new(int)
	*y = 1
}
