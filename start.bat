@echo off
title Threads Scraper
color 0A

:: Set script directory
cd /d "%~dp0"

:: Check results folder
if not exist "results" mkdir results

:: Check main file
if not exist "threads_scraper.py" (
    echo [ERROR] File threads_scraper.py not found!
    echo.
    pause
    exit /b 1
)

:: Run program
echo ========================================
echo    STARTING THREADS SCRAPER...
echo ========================================
echo.
python threads_scraper.py

:: If error
if errorlevel 1 (
    echo.
    echo ========================================
    echo    PROGRAM ERROR!
    echo ========================================
    echo.
    echo Check the following:
    echo 1. Internet connection
    echo 2. The entered Session ID
    echo 3. Dependencies (run setup.bat)
    echo.
)

echo.
echo Press any key to exit...
pause >nul
