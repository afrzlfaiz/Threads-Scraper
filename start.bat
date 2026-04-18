@echo off
title Threads Scraper
color 0A

:: Set ke direktori script
cd /d "%~dp0"

:: Cek folder results
if not exist "results" mkdir results

:: Cek file utama
if not exist "threads_scraper.py" (
    echo [ERROR] File threads_scraper.py tidak ditemukan!
    echo.
    pause
    exit /b 1
)

:: Jalankan program
echo ========================================
echo    MEMULAI THREADS SCRAPER...
echo ========================================
echo.
python threads_scraper.py

:: Jika error
if errorlevel 1 (
    echo.
    echo ========================================
    echo    PROGRAM ERROR!
    echo ========================================
    echo.
    echo Periksa kembali:
    echo 1. Koneksi internet
    echo 2. Session ID yang dimasukkan
    echo 3. Dependencies (jalankan setup.bat)
    echo.
)

echo.
echo Tekan tombol apapun untuk keluar...
pause >nul