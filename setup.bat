@echo off
echo ================================
echo Setting up QA Automation Project
echo ================================

echo.
echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .venv\Scripts\activate

echo.
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Installing Playwright browsers...
playwright install

echo.
echo Setup completed successfully!
pause