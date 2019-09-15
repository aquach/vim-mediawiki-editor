#!/bin/bash

# To run, put a credentials.json with a username and password field for
# Wikipedia. The test attempts to log in for you to test the mwclient login.

for f in *.Dockerfile
do
  echo "Building $f image..."
  sudo docker build -f $f -t ${f%.Dockerfile} ..
done

echo "Starting tests..."

for f in *.Dockerfile
do
  sudo docker run -i ${f%.Dockerfile} < credentials.json
done

echo "Tests complete."
