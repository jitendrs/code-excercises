/*
Simple go web-server example
*/

package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler) // each requests calls handler
	log.Fatal(http.ListenAndServe("localhost:8282", nil))
}

// handler echoes the Path component of the requests URL r.
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
	fmt.Fprintf(w, "This is Awesome")
}
