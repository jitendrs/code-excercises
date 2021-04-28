/*
Go program from The go programming language book page:72
Program: basename
Description: code to extract basename from filepath with suffix likes '/'
Example: a/b/c.go
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	fpath := string(os.Args[1:])
	fmt.Println(" File name is: ", fpath)
	for i := len(fpath) - 1; i >= 0; i-- {
		if fpath[i] == '/' {
			fmt.Print("I AM inside of loop")
			fpath = fpath[i+1:]
			break
		}
	}
	fmt.Println(" File name is: ", fpath)

	for i := len(fpath) - 1; i >= 0; i-- {
		if fpath[i] == '.' {
			fpath = fpath[:i]
			break
		}
	}
	fmt.Println(" File name is: ", fpath)
}
