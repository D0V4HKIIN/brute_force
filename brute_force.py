from pynput.keyboard import Key, Controller
import time
from pynput.mouse import Listener, Button

keyboard = Controller()
a = 0


def on_click(x, y, button, pressed):
    return pressed


def sendNext(i):

    print("sending", i)
    # keyboard.press(Key.ctrl)
    # keyboard.press("a")
    # keyboard.release("a")
    # keyboard.release(Key.ctrl)

    # time.sleep(0.1)
    keyboard.type(str(i))

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


i = 7000
while True:
    i += 1
    print(i)
    with Listener(on_click=on_click) as listener:
        listener.join()
        sendNext(i)
