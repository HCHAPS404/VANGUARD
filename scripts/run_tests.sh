#!/bin/bash
# 
# VANGUARD - Run Tests Script
# 
# Description:
#   This script is a wrapper to run the Pytest suite using `uv`.
#   It ensures that tests are run within the correct virtual environment
#   managed by `uv`, and allows passing additional arguments directly to pytest.
#
# Usage:
#   ./scripts/run_tests.sh [pytest arguments]
#
# Examples:
#   ./scripts/run_tests.sh                        # Run all tests
#   ./scripts/run_tests.sh -v                     # Run all tests with verbose output
#   ./scripts/run_tests.sh tests/test_schemas.py  # Run specific test file

set -e

echo "Running VANGUARD test suite..."
uv run pytest "$@"
