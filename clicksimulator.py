import pyautogui
import time
import pyperclip

# === SETTINGS ===
chrome_icon = (319.890625, 919.33203125)           # REPLACE with actual position of Chrome icon in taskbar
google_sheet_cell = (562.07421875, 357.14453125)      # REPLACE with cell containing LinkedIn link
linkedin_more = (475.06640625, 675.3046875)          # REPLACE with position of "More" button on LinkedIn
linkedin_connect = (850, 650)       # REPLACE with position of "Connect" button
report_button = (940.40625, 767.7265625)

# === START SCRIPT ===
def open_chrome_and_sheet(sheet_url):
    print("Opening Chrome and Google Sheet")
    pyautogui.click(chrome_icon)
    time.sleep(5)
    print("Chrome opened")
    # Open Google Sheet
    pyperclip.copy(sheet_url)
    pyautogui.hotkey('command', 'l')  # Focus address bar
    pyautogui.hotkey('command', 'v')  # Paste URL
    pyautogui.press('enter')
    time.sleep(5)
    print("Google Sheet opened")
    
def connect_one_person():
    print("Connecting to one person")
    # Click cell with LinkedIn link
    pyautogui.click(google_sheet_cell)
    time.sleep(5)
    pyautogui.hotkey('command', 'c')  # Copy link
    time.sleep(5)

    # Paste link into new tab
    pyautogui.hotkey('command', 't')  # New tab
    time.sleep(5)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')
    time.sleep(5)
    print("LinkedIn opened")
    # Click "More" and then "Connect"
    pyautogui.click(linkedin_more)
    time.sleep(5)
    pyautogui.click(linkedin_connect)
    time.sleep(5)
    pyautogui.click(report_button)
    time.sleep(5)
    print("More and Connect buttons clicked")
    # Close tab
    pyautogui.hotkey('command', 'w')
    time.sleep(5)
    print("Tab closed")
    # Scroll up in Google Sheet
    pyautogui.scroll(100)  # Scroll up one cell worth
    print("Scrolled up in Google Sheet")
# === RUN ===
print("Starting script...")
sheet_url = 'https://docs.google.com/spreadsheets/d/1V8FGC-CouHCMhFfxmWz1WpcJkdVgCCQBXj6m1_vEJe4/edit?gid=510585410#gid=510585410'  # REPLACE with your sheet URL
open_chrome_and_sheet(sheet_url)

print("Script started")
for i in range(10):  # Adjust for however many rows you want
    connect_one_person()
    print(f"Completed {i+1} connections")

print("Script completed")
