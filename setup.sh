#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "   THREADS SCRAPER - SETUP SCRIPT"
echo "========================================"
echo ""

# Check Python
echo "[1/4] Checking Python..."
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[OK] Python found${NC}"
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    echo -e "${GREEN}[OK] Python found${NC}"
    PYTHON_CMD="python"
else
    echo -e "${RED}[ERROR] Python not found!${NC}"
    echo "Please install Python first"
    exit 1
fi
$PYTHON_CMD --version
echo ""

# Check pip
echo "[2/4] Checking pip..."
if command -v pip3 &>/dev/null; then
    echo -e "${GREEN}[OK] pip found${NC}"
    PIP_CMD="pip3"
elif command -v pip &>/dev/null; then
    echo -e "${GREEN}[OK] pip found${NC}"
    PIP_CMD="pip"
else
    echo -e "${RED}[ERROR] pip not found!${NC}"
    exit 1
fi
echo ""

# Install requirements
echo "[3/4] Installing dependencies..."
echo "This may take a moment..."
$PIP_CMD install -r requirements.txt
if [ $? -ne 0 ]; then
    echo -e "${RED}[ERROR] Failed to install dependencies!${NC}"
    exit 1
fi
echo -e "${GREEN}[OK] Dependencies installed successfully${NC}"
echo ""

# Create results folder
echo "[4/4] Creating results folder..."
if [ ! -d "results" ]; then
    mkdir results
fi
echo -e "${GREEN}[OK] 'results' folder created${NC}"
echo ""

echo "========================================"
echo "   SETUP COMPLETE!"
echo "========================================"
echo ""
echo "Run the program with:"
echo "  ./start.sh"
echo ""
