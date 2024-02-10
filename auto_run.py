from configparser import ConfigParser
from os import path

import keyboard

from keyboard_simulator import PressKey, ReleaseKey, KEY_W, KEY_LSHIFT

is_active = False


def enter_run():
    global is_active

    print("w+shift are pressed")
    PressKey(KEY_W)
    PressKey(KEY_LSHIFT)
    is_active = True


def exit_run():
    global is_active

    print("w+shift are released")
    ReleaseKey(KEY_W)
    ReleaseKey(KEY_LSHIFT)
    is_active = False


def toggle_run(*args, **kwargs):
    global is_active

    print(f"toggle key was pressed...")
    if is_active:
        exit_run()
    else:
        enter_run()


def main():
    if path.exists("settings.ini"):
        config = ConfigParser()
        config.read("settings.ini")
        toggle_key = config.get("bindings", "toggle_key", fallback="=")
    else:
        toggle_key = "="

    print(f"You can now enter the game | Toggle key: <{toggle_key}> | Exit program by: ctrl+c")

    try:
        keyboard.on_press_key(toggle_key, callback=toggle_run, suppress=True)
        keyboard.wait()
    except KeyboardInterrupt:
        print("Exited program")
    finally:
        exit_run()  # exit_run is here to release w and shift before closing, so they don't get stuck


if __name__ == "__main__":
    main()
