import sys #modify system encoding for better character support
import pyautogui #will help us send keyboard shortcuts
import time #introduce delays
import os #handles file paths and checks file existence

sys.stdout.reconfigure(encoding='utf-8')  # Ensure UTF-8 output

print("🔍 Monitoring for YouTube...")  # Script is monitoring now!

image_path = r"C:\DistractionStopsHere-main\DistractionStopsHere\youtube_dark.png" # Define the full image path for YouTube tab detection

if not os.path.exists(image_path): # Checks if the image file exists in the path
    print(f"Error: The image '{image_path}' does not exist.") #if not
    exit() 

while True: #infinite loop
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
            print("🔍 YouTube not detected. Monitoring...") #continue to monitor if YouTube isnt found
        
    except pyautogui.ImageNotFoundException:
        print("⚠️ Image not found on the screen. Ensure the image is correct.") #catch and handle exceptions if image detection fails
    
    time.sleep(1)  # Check every 1 second
