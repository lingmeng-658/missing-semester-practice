#!/bin/bash
set -euo pipefail

LOGFILE="test_runs_$(date +%s).log"
echo "Logging to $LOGFILE"

RUN=1

while "$@" > "$LOGFILE" 2>&1; do
  echo "Run $RUN passed"
  RUN=$((RUN + 1))
done

echo "Test failed on run $RUN"
echo "Last 20 lines of output:"
tail -n 20 "$LOGFILE"
echo "Full log: $LOGFILE"
