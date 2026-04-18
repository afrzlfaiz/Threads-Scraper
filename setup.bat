@echo off
title Threads Scraper Setup
echo ========================================
echo    THREADS SCRAPER - SETUP SCRIPT
echo ========================================
echo.

:: Cek Python
echo [1/4] Mengecek Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu dari https://python.org
    echo.
    pause
    exit /b 1
)
echo [OK] Python ditemukan
echo.

:: Cek pip
echo [2/4] Mengecek pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip tidak ditemukan!
    pause
    exit /b 1
)
echo [OK] pip ditemukan
echo.

:: Install requirements
echo [3/4] Menginstall dependencies...
echo Ini akan memakan waktu beberapa saat...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Gagal menginstall dependencies!
    pause
    exit /b 1
)
echo [OK] Dependencies berhasil diinstall
echo.

:: Buat folder untuk hasil
echo [4/4] Membuat folder untuk hasil...
if not exist "results" mkdir results
echo [OK] Folder 'results' telah dibuat
echo.

echo ========================================
echo    SETUP SELESAI!
echo ========================================
echo.
echo Jalankan program dengan:
echo   start.bat
echo.
pause