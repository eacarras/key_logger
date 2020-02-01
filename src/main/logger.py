from pynput import keyboard
import sys
sys.path.append('../')
from utils.time import LogDate

def on_press(key):
    if str(key) == 'Key.esc':
        sys.exit()
    else:
        print(f'{LogDate().Year()} | {LogDate().Hour()} {key}')

with keyboard.Listener(
    on_press=on_press) as key_listener:
    key_listener.join()