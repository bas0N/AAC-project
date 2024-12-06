@echo off
REM Check if "py" command exists
where py >nul 2>nul
if %errorlevel%==0 (
    REM If "py" is available, use it
    py index.nbconvert.py
) else (
    REM Otherwise, fallback to "python"
    python index.nbconvert.py
)

pause
