
import pyautogui
import time

# Set the time interval between clicks in seconds
interval = 5

print(f"Auto-clicking every {interval} seconds. Press Ctrl+C to stop.")

try:
    while True:
        # Perform a left mouse click
        pyautogui.click()

        # Pause the program for the specified interval
        time.sleep(interval)
except KeyboardInterrupt:
    print("Program stopped.")