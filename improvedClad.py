from pynput import keyboard
from pynput.mouse import Controller, Button

# Initialize the mouse controller
mouse = Controller()

# Global variable to track whether mouse control is active
mouse_speed = 20  # Default mouse speed

# A set to keep track of pressed keys
current_keys = set()

def on_press(key):
    global mouse_speed

    # Add pressed key to current_keys set
    current_keys.add(key)

    # Modifier key for Alt
    is_alt_pressed = keyboard.Key.alt in current_keys or keyboard.Key.alt_l in current_keys

    # If Alt is pressed, map the movement and action keys
    if is_alt_pressed:
        if key == keyboard.KeyCode(char='i'):  # Move mouse up
            mouse.move(0, -mouse_speed)
        elif key == keyboard.KeyCode(char='k'):  # Move mouse down
            mouse.move(0, mouse_speed)
        elif key == keyboard.KeyCode(char='j'):  # Move mouse left
            mouse.move(-mouse_speed, 0)
        elif key == keyboard.KeyCode(char='l'):  # Move mouse right
            mouse.move(mouse_speed, 0)
        elif key == keyboard.KeyCode(char='u'):  # Left Click
            mouse.click(Button.left)
        elif key == keyboard.KeyCode(char='o'):  # Right Click
            mouse.click(Button.right)
        elif key == keyboard.KeyCode(char='p'):  # Scroll Up
            mouse.scroll(0, 1)
        elif key == keyboard.KeyCode(char=';'):  # Scroll Down
            mouse.scroll(0, -1)

def on_release(key):
    # Remove released key from current_keys
    current_keys.discard(key)

# Listener to listen for key presses and releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
