from pynput.mouse import Listener

# Function to print mouse coordinates
def print_coordinates(x, y):
    print(f'Mouse coordinates: ({x}, {y})')

# Function to handle mouse movement
def on_move(x, y):
    print_coordinates(x, y)

# Function to handle mouse click
def on_click(x, y, button, pressed):
    if pressed:
        print_coordinates(x, y)

# Function to handle mouse scroll
def on_scroll(x, y, dx, dy):
    print_coordinates(x, y)

# Main function
def main():
    # Start listening for mouse events
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        print("Mouse logging started. Press Ctrl+C to stop.")
        listener.join()

if __name__ == "__main__":
    main()
