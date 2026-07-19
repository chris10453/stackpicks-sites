#!/usr/bin/env bash
# Grep-style release gate: every canonical PawWise Brain Training page must say $67 and no stale $47.
set -euo pipefail
BASE="${1:-https://stackpicks.net/pawwise}"
for page in index.html best-online-dog-training-programs.html brain-training-for-dogs-review.html brain-training-for-dogs-vs-doggy-dan.html; do
  body=$(curl -fsSL "$BASE/$page")
  grep -q '\$67' <<<"$body" || { echo "FAIL: $page missing \\$67"; exit 1; }
  if grep -q '\$47' <<<"$body"; then echo "FAIL: $page contains stale \\$47"; exit 1; fi
done
echo 'PRICE-CONSISTENCY: PASS ($67 across 4 canonical pages)'
