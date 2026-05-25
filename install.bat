@echo off
echo Installing backend...
cd backend
pip install -r requirements.txt

echo Installing frontend...
cd ..\frontend
npm install

echo Done.
pause