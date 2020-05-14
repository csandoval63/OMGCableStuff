[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
wget "https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe" -outfile "python-3.8.0.exe"
.\python-3.8.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
Start-Sleep -s 40
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
Remove-Item .\python-3.8.0.exe
invoke-expression 'cmd /c start powershell -Command { mode con:cols=18 lines=1; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User"); python -m pip install --upgrade pip; pip install wheel; pip install pynput; pip install pywin32; pip install requests; pip install easygui }'
