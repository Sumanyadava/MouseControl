from pynput import keyboard
from pynput.mouse import Controller, Button
import os

# Initialize the mouse controller
mouse = Controller()

# Global variable to track whether mouse control is active
mouse_control_active = False
mouse_speed = 20  # Default mouse speed

# Hotkeys for activating mouse control and closing it
toggle_hotkey = {keyboard.Key.ctrl_l, keyboard.Key.space}  # Ctrl + Space

# A set to keep track of pressed keys
current_keys = set()

# Path to the .Xmodmap file
xmodmap_file = os.path.expanduser("~/.Xmodmap")

def toggle_mouse_control():
    """
    Toggle the state of mouse control (on/off) and apply/remove key suppression.
    """
    global mouse_control_active
    mouse_control_active = not mouse_control_active
    if mouse_control_active:
        print("Mouse control activated")
        apply_xmodmap()  # Suppress keys
    else:
        print("Mouse control deactivated")
        reset_xmodmap()  # Restore keys

def apply_xmodmap():
    """
    Apply the key suppression by running the xmodmap command.
    """
    os.system(f"xmodmap {xmodmap_file}")

def reset_xmodmap():
    """
    Reset the key mappings by removing the suppression.
    """
    # This command reloads the default keymap
    os.system("setxkbmap")

def on_press(key):
    """
    Handle key press events:
    - Toggles mouse control with Ctrl + Space.
    - If mouse control is active, moves the mouse or triggers mouse actions.
    """
    global mouse_control_active, mouse_speed
    
    # Track the currently pressed keys
    current_keys.add(key)

    # Check if the toggle hotkey (Ctrl + Space) is pressed to activate or deactivate mouse control
    if toggle_hotkey.issubset(current_keys):
        toggle_mouse_control()

    # If mouse control is active, perform mouse-related actions
    if mouse_control_active:
        if key == keyboard.Key.up:
            mouse.move(0, -mouse_speed)  # Move mouse up
        elif key == keyboard.Key.down:
            mouse.move(0, mouse_speed)  # Move mouse down
        elif key == keyboard.Key.left:
            mouse.move(-mouse_speed, 0)  # Move mouse left
        elif key == keyboard.Key.right:
            mouse.move(mouse_speed, 0)  # Move mouse right
        
        # Perform mouse actions
        elif key == keyboard.Key.insert:  # Left click
            mouse.click(Button.left)
        elif key == keyboard.Key.home:  # Right click
            mouse.click(Button.right)
        elif key == keyboard.Key.page_up:  # Scroll up
            mouse.scroll(0, 1)
        elif key == keyboard.Key.page_down:  # Scroll down
            mouse.scroll(0, -1)
        elif key == keyboard.Key.end:  # Increase speed
            mouse_speed = 100  # Set speed to maximum (100)

def on_release(key):
    """
    Handle key release events:
    - Remove the key from the set of currently pressed keys.
    """
    # Remove the released key from the set of pressed keys
    current_keys.discard(key)

# Listener to listen for key presses and releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    """
    Starts listening for key events:
    - Calls on_press() when a key is pressed.
    - Calls on_release() when a key is released.
    """
    listener.join()  # Keeps the program running, listening for key events
