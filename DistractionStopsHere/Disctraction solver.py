import pyautogui
import time
import os

# Define the full image path for YouTube detection
image_path = r"C:\DistractionStopsHere\youtube_dark.png"


if not os.path.exists(image_path): # Checks if the image file exists
    print(f"Error: The image '{image_path}' does not exist.")
    exit()

print("🔍 Monitoring for YouTube...")

while True:
    try:
        # Try locating the YouTube tab image
        screenShot = pyautogui.locateCenterOnScreen(image_path, confidence=0.6, grayscale=True) # Locate the YouTube tab image
        if screenShot:
            print(f"✅ YouTube detected at: {screenShot}")
            time.sleep(1)  # Pause before executing the shortcut
            pyautogui.hotkey('ctrl', 'w')  # Closes the current tab
            print("🛑 Closed YouTube tab successfully!")
            time.sleep(5)  # Wait 5 seconds before scanning again to prevent instant re-closing
        else:
            print("🔍 YouTube not detected. Monitoring...")
        
    except pyautogui.ImageNotFoundException:
        print("⚠️ Image not found on the screen. Ensure the image is correct.")
    
    time.sleep(1)  # Check every 1 second
