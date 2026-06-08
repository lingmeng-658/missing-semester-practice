#!/bin/bash
set -x

name="lingmeng"
file="notes.txt"

echo "hello $name"
echo "this is a note">"$file"
cat "$file"
