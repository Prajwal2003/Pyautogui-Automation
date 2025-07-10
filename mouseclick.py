from pynput import mouse

click_count = 0  # Global counter

def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1
        print(f"Mouse clicked at ({x}, {y})")
        if click_count >= 4:
            # Stop listener after 4 clicks
            return False

# Start the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
