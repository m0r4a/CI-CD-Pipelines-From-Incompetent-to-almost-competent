package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type RequestPayload struct {
	Name string `json:"name"`
}

type ResponsePayload struct {
	Greet string `json:"greet"`
}

func greedHandler (w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Forbidden method", http.StatusMethodNotAllowed)
		return
	}

	var requestData RequestPayload

	err := json.NewDecoder(r.Body).Decode(&requestData)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	greet := fmt.Sprintf("Hi, %s greetings from Go!", requestData.Name)
	responseData := ResponsePayload{Greet: greet}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(responseData)
}

func main() {
	http.HandleFunc("/greet", greedHandler)	
	fmt.Println("Go server listening on http://localhost:8088")
	http.ListenAndServe(":8088", nil)
}
