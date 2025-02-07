import sys
import pyautogui
import time
import os

sys.stdout.reconfigure(encoding='utf-8')

# Define a dictionary of sites and their corresponding image paths
site_images = {
    "YouTube": r"C:\DistractionStopsHere-main\DistractionStopsHere\youtube_dark.png",
    "Facebook": r"C:\DistractionStopsHere-main\DistractionStopsHere\facebook_dark.png",
    "Instagram": r"C:\DistractionStopsHere-main\DistractionStopsHere\instagram_light.png"
}
# Check if all image files exist before starting
missing_images = [site for site, path in site_images.items() if not os.path.exists(path)]
if missing_images:
    print(f"❌ Error: Image(s) not found for {', '.join(missing_images)}. Please check file paths.")
    exit()
print("🔍 Monitoring for distracting websites...")
while True:
    try:
        for site, image_path in site_images.items():
            # Try locating the image for the current site
            screenShot = pyautogui.locateCenterOnScreen(image_path, confidence=0.6, grayscale=False)
            if screenShot:
                print(f"✅ {site} detected at: {screenShot}")
                time.sleep(1)  # Pause before closing
                pyautogui.hotkey('ctrl', 'w')  # Close the current tab
                print(f"🛑 Closed {site} successfully!")
                time.sleep(5)  # Wait 5 seconds to prevent immediate re-opening
            else:
                print(f"🔍 {site} not detected. Monitoring...")
    except pyautogui.ImageNotFoundException:
        print("⚠️ Image not found on the screen. Ensure the image is correct.")
    time.sleep(1)  # Check again after 1 second
