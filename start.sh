#!/bin/bash

# Warna untuk output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Set ke direktori script
cd "$(dirname "$0")"

# Cek folder results
if [ ! -d "results" ]; then
    mkdir results
fi

# Cek file utama
if [ ! -f "threads_scraper.py" ]; then
    echo -e "${RED}[ERROR] File threads_scraper.py tidak ditemukan!${NC}"
    exit 1
fi

# Tentukan perintah Python
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Clear screen
clear

# Jalankan program
echo "========================================"
echo "   MEMULAI THREADS SCRAPER..."
echo "========================================"
echo ""

$PYTHON_CMD threads_scraper.py

# Jika error
if [ $? -ne 0 ]; then
    echo ""
    echo "========================================"
    echo "   PROGRAM ERROR!"
    echo "========================================"
    echo ""
    echo "Periksa kembali:"
    echo "1. Koneksi internet"
    echo "2. Session ID yang dimasukkan"
    echo "3. Dependencies (jalankan ./setup.sh)"
    echo ""
    echo "Tekan Enter untuk keluar..."
    read
fi