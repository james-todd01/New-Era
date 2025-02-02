import time
from helium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from seleniumbase import SB

try:
    with SB(uc=True, incognito=False) as sb:
        driver = sb.driver
    
        # Open the Xfinity login page (or any page you want to scrape)
        url = "https://login.xfinity.com/login"
        sb.driver.uc_open_with_reconnect(url, 3)
        set_driver(driver)
        time.sleep(5)
        if Button("Accept All").exists():
            click(Button("Accept All"))
        count = 5
        item = "nksilva@comcast.net"
        while count:
            try:
                if not Text("Sign in with your Xfinity ID").exists():
                    driver.get("https://login.xfinity.com/login")
                time.sleep(2)
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[tag="h1"]'))
                )
                # print('Login screen updated')
                if Button("Decline All").exists():
                    click(Button("Decline All"))
                if Text("Sign in with your Xfinity ID").exists():
                    username_field = driver.find_element(By.ID, 'user')
                    username_field.send_keys(item.strip())
                    time.sleep(1)
                    # print('email id entered')
                    # username_field.send_keys(Keys.RETURN)
                    # screenshot_path = '/content/drive/My Drive/screenshot1.png'
                    # driver.save_screenshot(screenshot_path)
                    driver.find_element(By.ID, 'sign_in').click()
                    time.sleep(1)
                    if driver.title == "Please reset your Xfinity password":
                        print("Inactive ID detected")
                    elif Text("Enter your password").exists():
                        print("Active ID detected")
                    elif Text('The Xfinity ID you entered was incorrect. Please try again.').exists():
                        print("Suspicious ID detected")
                    else:
                        print("Throttling Detected")
                        count -= 1
            except Exception as error:
                time.sleep(4)
                if Button("Decline All").exists():
                    click(Button("Decline All"))
except Exception as e_rror:
    print(f'Thread error ocuured.Error: {e_rror}')
