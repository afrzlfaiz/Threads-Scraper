@echo off
title Threads Scraper Setup
echo ========================================
echo    THREADS SCRAPER - SETUP SCRIPT
echo ========================================
echo.

:: Check Python
echo [1/4] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python first from https://python.org
    echo.
    pause
    exit /b 1
)
echo [OK] Python found
echo.

:: Check pip
echo [2/4] Checking pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip not found!
    pause
    exit /b 1
)
echo [OK] pip found
echo.

:: Install requirements
echo [3/4] Installing dependencies...
echo This may take a moment...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)
echo [OK] Dependencies installed successfully
echo.

:: Create results folder
echo [4/4] Creating results folder...
if not exist "results" mkdir results
echo [OK] 'results' folder created
echo.

echo ========================================
echo    SETUP COMPLETE!
echo ========================================
echo.
echo Run the program with:
echo   start.bat
echo.
pause
