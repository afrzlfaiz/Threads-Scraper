#!/bin/bash

# Warna untuk output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "   THREADS SCRAPER - SETUP SCRIPT"
echo "========================================"
echo ""

# Cek Python
echo "[1/4] Mengecek Python..."
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[OK] Python ditemukan${NC}"
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    echo -e "${GREEN}[OK] Python ditemukan${NC}"
    PYTHON_CMD="python"
else
    echo -e "${RED}[ERROR] Python tidak ditemukan!${NC}"
    echo "Silakan install Python terlebih dahulu"
    exit 1
fi
$PYTHON_CMD --version
echo ""

# Cek pip
echo "[2/4] Mengecek pip..."
if command -v pip3 &>/dev/null; then
    echo -e "${GREEN}[OK] pip ditemukan${NC}"
    PIP_CMD="pip3"
elif command -v pip &>/dev/null; then
    echo -e "${GREEN}[OK] pip ditemukan${NC}"
    PIP_CMD="pip"
else
    echo -e "${RED}[ERROR] pip tidak ditemukan!${NC}"
    exit 1
fi
echo ""

# Install requirements
echo "[3/4] Menginstall dependencies..."
echo "Ini akan memakan waktu beberapa saat..."
$PIP_CMD install -r requirements.txt
if [ $? -ne 0 ]; then
    echo -e "${RED}[ERROR] Gagal menginstall dependencies!${NC}"
    exit 1
fi
echo -e "${GREEN}[OK] Dependencies berhasil diinstall${NC}"
echo ""

# Buat folder untuk hasil
echo "[4/4] Membuat folder untuk hasil..."
if [ ! -d "results" ]; then
    mkdir results
fi
echo -e "${GREEN}[OK] Folder 'results' telah dibuat${NC}"
echo ""

echo "========================================"
echo "   SETUP SELESAI!"
echo "========================================"
echo ""
echo "Jalankan program dengan:"
echo "  ./start.sh"
echo ""