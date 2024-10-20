from pynput import keyboard
from pynput.mouse import Controller, Button

# Initialize the mouse controller
mouse = Controller()

# Global variable to track whether mouse control is active
mouse_control_active = False
mouse_speed = 20  # Default mouse speed
drag_active = False  # Track drag status

# A set to keep track of pressed keys
current_keys = set()

# Define key mappings
key_mappings = {
    'toggle_mouse': keyboard.Key.pause,    # Toggle mouse control
    'move_up': keyboard.KeyCode(char='i'),  # Move mouse up
    'move_down': keyboard.KeyCode(char='k'),  # Move mouse down
    'move_left': keyboard.KeyCode(char='j'),  # Move mouse left
    'move_right': keyboard.KeyCode(char='l'),  # Move mouse right
    'left_click': keyboard.KeyCode(char='u'),  # Left click
    'drag_start': keyboard.KeyCode(char='y'),   # Start drag (Alt + Y)
    'drag_stop': keyboard.KeyCode(char='n'),    # Stop drag (Alt + N)
    'right_click': keyboard.KeyCode(char='o'),  # Right click
    'scroll_up': keyboard.KeyCode(char='p'),     # Scroll up
    'scroll_down': keyboard.KeyCode(char=';'),   # Scroll down
    'escape': keyboard.Key.esc                    # Escape key
}

def toggle_mouse_control():
    global mouse_control_active
    mouse_control_active = not mouse_control_active
    print("Mouse control activated" if mouse_control_active else "Mouse control deactivated")

def on_press(key):
    global mouse_speed, drag_active

    # Add pressed key to current_keys set
    current_keys.add(key)

    # Toggle mouse control
    if key == key_mappings['toggle_mouse']:
        toggle_mouse_control()

    # If mouse control is active and Alt key is pressed, check for movement keys
    if mouse_control_active:
        is_alt_pressed = keyboard.Key.alt in current_keys or keyboard.Key.alt_l in current_keys

        if is_alt_pressed:
            if key == key_mappings['move_up']:
                mouse.move(0, -mouse_speed)  # Move mouse up
            elif key == key_mappings['move_down']:
                mouse.move(0, mouse_speed)  # Move mouse down
            elif key == key_mappings['move_left']:
                mouse.move(-mouse_speed, 0)  # Move mouse left
            elif key == key_mappings['move_right']:
                mouse.move(mouse_speed, 0)  # Move mouse right
            
            # Left Click (Alt + U)
            elif key == key_mappings['left_click']:
                mouse.click(Button.left)
                print("Left Click executed")
            
            # Start Drag (Alt + Y)
            elif key == key_mappings['drag_start'] and not drag_active:
                mouse.press(Button.left)
                drag_active = True
                print("Drag started")
            
            # Stop Drag (Alt + H)
            elif key == key_mappings['drag_stop'] and drag_active:
                mouse.release(Button.left)
                drag_active = False
                print("Drag stopped")
            
            # Right Click
            elif key == key_mappings['right_click']:
                mouse.click(Button.right)
            
            # Scroll Up
            elif key == key_mappings['scroll_up']:
                mouse.scroll(0, 1)
            
            # Scroll Down
            elif key == key_mappings['scroll_down']:
                mouse.scroll(0, -1)

def on_release(key):
    # Remove released key from current_keys
    current_keys.discard(key)

    # Exit on Escape key press
    if key == key_mappings['escape']:
        return False

# Listener to listen for key presses and releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
