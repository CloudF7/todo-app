@echo off
pyinstaller --onefile --windowed app1\main.py --distpath app1\dist --workpath app1\build --specpath app1
pause