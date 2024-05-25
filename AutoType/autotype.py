import pyautogui
import time
import sys
import keyboard

def type_text(text, interval=0.01):

    for char in text:
        if keyboard.is_pressed('esc'):  # Stop typing if 'esc' key is pressed
            print("\nTyping stopped by user.")
            break

        pyautogui.press('delete') # Press 'Delete' to remove any auto-completion suggestions

        if char == '\n':
            pyautogui.press('enter') # Press 'Enter' to go to a new line
            pyautogui.press('home') # Moves the cursor on the very beginning of the line
        else:
            pyautogui.typewrite(char)

        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python autotype.py <text-to-type|file-path> [typing-speed-interval]")
        sys.exit(1)

    input_source = sys.argv[1]
    typing_speed_interval = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01

    # Determine if input_source is a file path or direct text
    try:
        with open(input_source, 'r') as file:
            text_to_type = file.read()
    except FileNotFoundError:
        text_to_type = input_source

    print(f"Typing text with interval: {typing_speed_interval}s")

    # Giving user 5 seconds to switch to the desired window
    time.sleep(5)

    type_text(text_to_type, typing_speed_interval)

