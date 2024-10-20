from pynput import keyboard

# Create a keyboard controller to simulate typing
keyboard_controller = keyboard.Controller()

def on_press(key):
    try:
        # Check if the key pressed is 'w'
        if key.char == 'w':
            # Simulate typing 's' when 'w' is pressed
            keyboard_controller.press('s')  # Press 's'
            keyboard_controller.release('s')  # Release 's'
            return False  # Block the original 'w' key press

    except AttributeError:
        # Handle special keys (like Ctrl, Shift, etc.)
        pass
    


# Start listening for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Keep the listener running indefinitely

    