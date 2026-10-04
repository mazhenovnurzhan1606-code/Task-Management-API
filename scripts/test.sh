#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 -m unittest discover -s tests -v 2>&1 | tee /tmp/test_output.txt

total=$(sed -n 's/^Ran \([0-9]*\) test.*/\1/p' /tmp/test_output.txt)

if grep -q '^OK' /tmp/test_output.txt; then
    passed=$total
else
    passed=0
fi

echo "TESTS: $passed/$total"