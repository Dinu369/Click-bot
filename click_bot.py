import pyautogui
import time
import random
import ctypes

# Minimize CMD window
def minimize_cmd():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 6)

minimize_cmd()

# Screen coordinates for buttons (adjust these to match your screen + browser zoom)
click_positions = [
    (281, 723), (285, 645), (268, 578), (122, 565), 
    (136, 472), (166, 538), (154, 611), (135, 590), 
    (93, 666), (117, 741)
]

print("🟢 Click bot started! Move mouse to (0,0) to stop.")

try:
    while True:
        for pos in click_positions:
            num_clicks = random.randint(8, 15)  # Vary clicks for each spot
            print(f"🖱️ Clicking {num_clicks} times at {pos}")

            for _ in range(num_clicks):
                pyautogui.moveTo(pos[0] + random.randint(-3, 3), pos[1] + random.randint(-3, 3))  # Small randomness
                pyautogui.click()
                time.sleep(random.uniform(0.03, 0.08))  # Slight delay between clicks

            if pyautogui.position() == (0, 0):
                print("\n🛑 Bot stopped by user.")
                exit()

        time.sleep(random.uniform(0.5, 1.0))  # Slight delay between rounds

except KeyboardInterrupt:
    print("\n🛑 Bot stopped manually.")
