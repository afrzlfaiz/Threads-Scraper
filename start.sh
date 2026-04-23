#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Set script directory
cd "$(dirname "$0")"

# Check results folder
if [ ! -d "results" ]; then
    mkdir results
fi

# Check main file
if [ ! -f "threads_scraper.py" ]; then
    echo -e "${RED}[ERROR] File threads_scraper.py not found!${NC}"
    exit 1
fi

# Determine Python command
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Clear screen
clear

# Run program
echo "========================================"
echo "   STARTING THREADS SCRAPER..."
echo "========================================"
echo ""

$PYTHON_CMD threads_scraper.py

# If error
if [ $? -ne 0 ]; then
    echo ""
    echo "========================================"
    echo "   PROGRAM ERROR!"
    echo "========================================"
    echo ""
    echo "Check the following:"
    echo "1. Internet connection"
    echo "2. The entered Session ID"
    echo "3. Dependencies (run ./setup.sh)"
    echo ""
    echo "Press Enter to exit..."
    read
fi
