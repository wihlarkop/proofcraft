package service

import (
	"encoding/json"
	"errors"
	"net/http"
)

var ErrMissing = errors.New("resource missing")

type Problem struct {
	Type   string `json:"type"`
	Title  string `json:"title"`
	Status int    `json:"status"`
}

func writeProblem(w http.ResponseWriter, status int, kind, title string) {
	w.Header().Set("Content-Type", "application/problem+json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(Problem{Type: kind, Title: title, Status: status})
}

func writeFailure(w http.ResponseWriter, err error) {
	if errors.Is(err, ErrMissing) {
		writeProblem(w, 404, "urn:problem:resource-missing", "Resource missing")
		return
	}
	writeProblem(w, 500, "urn:problem:internal", "Unable to complete request")
}
