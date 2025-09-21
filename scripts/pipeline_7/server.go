package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello world!")
}

func main() {
	var port string = "8888"
	http.HandleFunc("/", handler)

	fmt.Printf("Server listening on port %s...", port)

	log.Fatal(http.ListenAndServe(":" + port, nil))
}
