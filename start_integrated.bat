@echo off
echo ========================================
echo   S2S - Scrap to Spark - Battery Evaluation System
echo ========================================
echo.

echo Checking system requirements...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://python.org
    pause
    exit /b 1
)

REM Check if Node.js is available
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Node.js is not installed or not in PATH
    echo Please install Node.js 18+ from https://nodejs.org
    pause
    exit /b 1
)

echo ✅ System requirements met
echo.

REM Install backend dependencies if needed
echo Installing backend dependencies...
cd backend
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install backend dependencies
    pause
    exit /b 1
)

REM Create reports directory
if not exist "reports" mkdir reports

REM Install frontend dependencies if needed
echo Installing frontend dependencies...
cd ../frontend
if not exist "node_modules" (
    npm install
    if errorlevel 1 (
        echo ❌ Failed to install frontend dependencies
        pause
        exit /b 1
    )
)

REM Build frontend
echo Building frontend...
npm run build
if errorlevel 1 (
    echo ❌ Frontend build failed
    pause
    exit /b 1
)

cd ..

echo.
echo ========================================
echo   Starting S2S - Scrap to Spark Development Server
echo ========================================
echo.
echo 🚀 Backend will run on: http://localhost:8000
echo 🌐 Frontend will run on: http://localhost:8000 (integrated)
echo.
echo 📋 Features available:
echo    • Battery RUL Prediction
echo    • Deployment Recommendations  
echo    • Sustainability Analysis
echo    • AI-Powered Reports
echo    • PDF Report Downloads
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the integrated server
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause
