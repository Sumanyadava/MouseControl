from pynput import keyboard, mouse
from pynput.mouse import Button, Controller as MouseController

# Create a mouse controller object
mouse = MouseController()

# Speed settings
default_speed = 10
boosted_speed = 30
mouse_speed = default_speed

# Variables to track state
dragging = False
active = False  # Track if mouse control is active

def move_pointer(key):
    """Move the pointer with WASD keys."""
    current_position = mouse.position
    if key == 'w':
        mouse.position = (current_position[0], current_position[1] - mouse_speed)
    elif key == 'a':
        mouse.position = (current_position[0] - mouse_speed, current_position[1])
    elif key == 's':
        mouse.position = (current_position[0], current_position[1] + mouse_speed)
    elif key == 'd':
        mouse.position = (current_position[0] + mouse_speed, current_position[1])

def perform_left_click():
    """Perform a left-click."""
    mouse.click(Button.left, 1)

def perform_right_click():
    """Perform a right-click."""
    mouse.click(Button.right, 1)

def scroll_up():
    """Scroll up."""
    mouse.scroll(0, 1)  # Scroll up

def scroll_down():
    """Scroll down."""
    mouse.scroll(0, -1)  # Scroll down

def toggle_mouse_control():
    """Toggle the activation of mouse control."""
    global active
    active = not active
    print(f"Mouse control {'activated' if active else 'deactivated'}")

def on_press(key):
    global dragging, mouse_speed, active

    # Check if Pause key is pressed to toggle mouse control
    if key == keyboard.Key.pause:
        toggle_mouse_control()

    # If control is not active, do nothing
    if not active:
        return

    try:
        # Pointer movement with WASD
        if hasattr(key, 'char') and key.char in ['w', 'a', 's', 'd']:
            # Set mouse speed based on case
            mouse_speed = boosted_speed if key.char.isupper() else default_speed
            move_pointer(key.char)  # Move while dragging

        # Left-click with Q (Start dragging if Q is held)
        if key == keyboard.KeyCode.from_char('q'):
            if not dragging:
                # Start dragging
                dragging = True
                perform_left_click()  # Click down
                print("Drag is active now.")

        # Right-click with E
        if key == keyboard.KeyCode.from_char('e'):
            perform_right_click()  # Simulate right click

        # Scroll up with R
        if key == keyboard.KeyCode.from_char('r'):
            scroll_up()  # Scroll up

        # Scroll down with F
        if key == keyboard.KeyCode.from_char('f'):
            scroll_down()  # Scroll down

    except AttributeError:
        pass

def on_release(key):
    global dragging, mouse_speed, active

    # Stop the listener if ESC is pressed
    if key == keyboard.Key.esc:
        return False

    # Handle key releases
    if key == keyboard.KeyCode.from_char('q'):
        # Release drag and click
        if dragging:
            dragging = False
            mouse.release(Button.left)  # Release click
            print("Drag has ended.")

    # Reset speed after releasing WASD keys
    if hasattr(key, 'char') and key.char in ['w', 'a', 's', 'd']:
        mouse_speed = default_speed  # Reset to default speed when keys are released

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


    