package service

import "net/http"

// Two legacy endpoints duplicate the accepted problem contract's missing-resource mapping.
// The explicit improvement scenario targets this duplication; ordinary onboarding does not.
func legacyGet(w http.ResponseWriter) {
	writeProblem(w, 404, "urn:problem:resource-missing", "Resource missing")
}

func legacyDelete(w http.ResponseWriter) {
	writeProblem(w, 404, "urn:problem:resource-missing", "Resource missing")
}
