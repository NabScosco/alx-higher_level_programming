#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL,
# and displays the body of the response with a custom header X-School-User-Id
curl -sH "X-School-User-Id: 98" "$1"

