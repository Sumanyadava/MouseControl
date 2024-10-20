from pynput import keyboard
from pynput.mouse import Controller

# Create a mouse controller object
mouse = Controller()

# Speed of mouse movement
mouse_speed = 20

def on_press(key):
    try:
        # Check if the key pressed is an arrow key and move the mouse accordingly
        if key == keyboard.Key.up:
            # Move the mouse up
            current_position = mouse.position
            mouse.position = (current_position[0], current_position[1] - mouse_speed)

        elif key == keyboard.Key.down:
            # Move the mouse down
            current_position = mouse.position
            mouse.position = (current_position[0], current_position[1] + mouse_speed)

        elif key == keyboard.Key.left:
            # Move the mouse left
            current_position = mouse.position
            mouse.position = (current_position[0] - mouse_speed, current_position[1])

        elif key == keyboard.Key.right:
            # Move the mouse right
            current_position = mouse.position
            mouse.position = (current_position[0] + mouse_speed, current_position[1])

    except AttributeError:
        # For special keys like function keys
        pass

def on_release(key):
    # Stop the listener if ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
