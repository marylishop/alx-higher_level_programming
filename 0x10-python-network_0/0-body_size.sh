#!/bin/bash

# Check if URL is provided as argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and get the size of the response body in bytes
SIZE=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')

# Display the size of the response body in bytes
echo "$SIZE"
