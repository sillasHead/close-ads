import pyautogui
import time

# Define the region to scan (left, top, width, height)
region_to_start = (1164, 108, 157, 81)
region_to_scan_icons_right = (1262, 108, 81, 59)
region_to_scan_icons_left = (598, 108, 161, 38)
region_to_return = (595, 70, 38, 33)
region_to_install = (595, 411, 743, 84)
region_to_handle_box = (595, 107, 749, 342)

def click_icon(name, icon_obj, click=None):
    try:
        icon = pyautogui.locateOnScreen(icon_obj[0], confidence=icon_obj[1], region=icon_obj[2])

        if click:
            click = pyautogui.locateOnScreen(click[0], confidence=click[1], region=click[2])

        if icon:
            click_position = click if click else pyautogui.center(icon)
            pyautogui.click(click_position)
            print(f"Clicked on the '{name}' icon!")
            # break  # Exit the loop after clicking
    except pyautogui.ImageNotFoundException:
        print(f"{name} icon not found. Checking next icon...")

def detect_icons():
    print("Monitoring the screen for icons... Press Ctrl+C to stop.")
    while True:
        try:
            pass_icon = ['img/pass-icon.png', 0.4, region_to_scan_icons_right]
            close_white_icon = ['img/white-x.png', 0.7, region_to_scan_icons_right]
            close_black_icon = ['img/black-x.png', 0.8]
            watch_icon = ['img/watch-ad.png', 0.6, region_to_start]

            install_icon = ['img/install.png', 0.8, region_to_install]
            return_icon = ['img/return.png', 0.8, region_to_return]

            box_screen_icon = ['img/box-screen.png', 0.8, region_to_handle_box]
            cancel_icon = ['img/cancel.png', 0.8, region_to_handle_box]

            click_icon("Pass", pass_icon)
            click_icon("Black Close", [*close_black_icon, region_to_scan_icons_left])
            click_icon("Black Close", [*close_black_icon, region_to_scan_icons_right])
            click_icon("White Close", close_white_icon)
            
            click_icon("Watch Ad", watch_icon)
            
            click_icon("Return", install_icon, return_icon)
            
            click_icon("Box", box_screen_icon)
            click_icon("Box", box_screen_icon, cancel_icon)

            # If no icons are found, retry after a delay
            print("No icon found. Retrying in 3 seconds...")
            time.sleep(3)

        except KeyboardInterrupt:
            print("Program stopped by user.")
            break

# Run the function
if __name__ == "__main__":
    detect_icons()
