#!/usr/bin/env bash

tmp="/tmp/mytemp.$$"

cleanup() {
  echo
  echo "Cleaning up temporary file: $tmp"
  rm -f "$tmp"
}

trap cleanup EXIT
trap 'echo; echo "Caught signal, exiting..."; exit 130' SIGINT SIGTERM

echo "temporary data" > "$tmp"
echo "Created temporary file: $tmp"
echo "Press Ctrl-C to stop this script."

sleep 1000
