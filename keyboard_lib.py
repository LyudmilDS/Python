from enum import Enum
import keyboard
import time


class keyboard_lib:
    movement_key_code = 1

    class MovementKey(Enum):
        w = 1
        a = 2
        s = 3
        d = 4

    def pressed_key(self, key):
        keyboard.press(key)
        keyboard.release(key)

    def press_hold_key(self, key):
        time.sleep(0.3)
        keyboard.press(key)
        time.sleep(0.3)
        keyboard.release(key)

    def fight_Graveler(self):
        print("fighting Graveler")
        # sleep functions are needed as the game has an animation before
        # every encounter and after each action
        time.sleep(1)
        self.pressed_key('1')
        time.sleep(1)
        self.pressed_key('1')
        time.sleep(2)

    def run(self):
        print("bad pokemon encountered. Running")
        # this sleep is needed as the game has an animation before every encounter
        time.sleep(1)
        self.pressed_key('4')
        time.sleep(1)

    def stop_program(self):
        if keyboard.is_pressed('esc'):
            print("Stop signal received. Program stopped")
            keyboard.wait('esc')
            return True
        return False

    def walking_in_circle(self):
        self.press_hold_key('w')
        self.press_hold_key('d')
        self.press_hold_key('s')
        self.press_hold_key('a')



