from pynput import keyboard, mouse
active = False

mouse_ctrl = mouse.Controller()

def on_press(key):
    """
    This function is called whenever a key is pressed.
    
    Parameters:
    - key: The key that was pressed.
    """
    global active  # Access the global 'active' variable

    if key == keyboard.Key.pause:
        active = not active  # Toggle the active state
        print(f"Mouse control {'activated' if active else 'deactivated'}")
        return  # Return after toggling, allowing other keys to be processed

    # If mouse control is active and the pressed key is a recognized character
    if active and hasattr(key, 'char') and key.char.lower() in 'wasdqerf':
        handle_mouse_action(key.char.lower())  # Handle the corresponding mouse action
        return False  # Prevent further processing of this key event

    return True  # Allow other keys to be processed

def handle_mouse_action(char):
    """
    Handle mouse actions based on the pressed character.
    
    Parameters:
    - char: The character corresponding to the key pressed.
    """
    speed = 10  # Set the default mouse movement speed

    # Check if the pressed key is for movement (WASD)
    if char in 'wasd':
        # Determine the change in mouse position (dx, dy) based on the pressed key
        dx, dy = {
            'a': (-speed, 0),  # Move left
            'd': (speed, 0),   # Move right
            'w': (0, -speed),  # Move up
            's': (0, speed)    # Move down
        }[char]
        mouse_ctrl.move(dx, dy)  # Move the mouse by the calculated amount

    # Handle mouse click actions
    elif char == 'q':
        mouse_ctrl.click(mouse.Button.left)  # Perform a left click
    elif char == 'e':
        mouse_ctrl.click(mouse.Button.right)  # Perform a right click

    # Handle scrolling actions
    elif char == 'r':
        mouse_ctrl.scroll(0, 1)  # Scroll up
    elif char == 'f':
        mouse_ctrl.scroll(0, -1)  # Scroll down

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Keep the listener running indefinitely
