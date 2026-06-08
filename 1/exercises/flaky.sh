#!/bin/bash

n=$((RANDOM % 5))

if [ "$n" -eq 0 ]; then
  echo "test failed"
  exit 1
else
  echo "test passed"
  exit 0
fi
