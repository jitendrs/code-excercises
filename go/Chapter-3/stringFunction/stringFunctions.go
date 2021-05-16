/*
Go program from The go programming language book page:69
Program: basic string functions
Description: code to check if string has prefix/suffix or provided substrings.
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	if HasPrefix(os.Args[1], os.Args[2]) {
		fmt.Printf("Prifix %s is in the string: %s\n", os.Args[1], os.Args[2])
	} else {
		fmt.Printf("Prifix %s is not the string: %s\n", os.Args[1], os.Args[2])
	}

	if HasSuffix(os.Args[1], os.Args[2]) {
		fmt.Printf("Sufix %s is in the string: %s\n", os.Args[2], os.Args[1])
	} else {
		fmt.Printf("Sufix %s is not the string: %s\n", os.Args[2], os.Args[1])
	}
	if Contains(os.Args[1], os.Args[2]) {
		fmt.Printf("string  %s is substring of : %s\n", os.Args[2], os.Args[1])
	} else {
		fmt.Printf("string  %s is not substring: %s\n", os.Args[2], os.Args[1])
	}
	fmt.Println(Index("adwdcddabcwew", "abc"))
}

func HasPrefix(s, prefix string) bool {
	return len(s) >= len(prefix) && s[:len(prefix)] == prefix
}

func HasSuffix(s, suffix string) bool {
	return len(s) >= len(suffix) && s[len(s)-len(suffix):] == suffix
}

func Contains(s, substr string) bool {
	for i := 0; i < len(s); i++ {
		if HasPrefix(s[i:], substr) {
			return true
		}
	}
	return false
}

func Index(s, sep string) int {
	for i := 0; i < len(s); i++ {
		if HasPrefix(s[i:], sep) {
			return i
		}
	}
	return -1
}
