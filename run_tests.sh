#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

mkdir -p reports

# Ensure tests can import from src/
export PYTHONPATH="${PYTHONPATH:-}:$ROOT/src"

STAMP="$(date +%Y-%m-%d_%H-%M-%S)"
pytest -v --maxfail=1   --html="reports/report_${STAMP}.html" --self-contained-html   --junitxml="reports/junit_${STAMP}.xml"
