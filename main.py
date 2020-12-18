#!/usr/bin/python3

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import datetime
import os

# Adding geckodriver to path temporarily.
# Works in Linux 64 bit only for now.
import set_geckodriver_path
set_geckodriver_path.add_geckodriver_to_PATH()

import scrape_webpage_contents
import generate_report

message = """
This program will generate a report of all the items you bought in Shopee.
I don't save any userdata in this program. I just automated the process.

You just provide the username/email, password and the OTP then the program
will automatically parse out all the information needed.

Rom Negrillo
github.com/romnegrillo
"""

def login(username_email, password, driver):
    """
    This function accepts email or username and and password along 
    with the selenium driver. Returns true if login is success.
    False otherwise. This will only login to see the page mobile
    verification.
    """
    
    # Wait until elemen with attribute name loginKey appears.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "loginKey")))

    # If loginKey is present, the element with attribute name password also exist,
    # we set the value of this element to be the username_email and password respectively.
    driver.find_element_by_name("loginKey").send_keys(username_email)
    driver.find_element_by_name("password").send_keys(password)

    # Wait until login element with a specific class value appears.
    # Using XPATH format:
    # "//element_name[@atteibute_name=value]" 
    # Example: <button class="_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y']")))

    # If the button exists, we click it. This emulates login button with the values we provided.
    driver.find_element_by_xpath("//button[@class='_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y']").click()

    # The page will load. The element with attribute name "autocomplete" and value "one-time-code" should appear.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="one-time-code"]')))

    # We get the html source of the current page and
    # we chekc if the text "Your verification code is sent by SMS to your phone" appears.

    html_source = driver.page_source

    if "Your verification code is sent by SMS to your phone" in html_source:
        return True

    return False 

def mobile_verification(mobile_verification_number, driver):
    """
    This function will be called if you the login to website was success and we need
    to enter verification code.
    """

    # Wait for the onetimecode element to appear which can be found with input element with autocomplete name attribute
    # then send verfication number in it.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="one-time-code"]')))
    driver.find_element_by_xpath('//input[@autocomplete="one-time-code"]').send_keys(mobile_verification_number)

    # Wait for the verification button to appear then perform submit action.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='_35rr5y _32qX4k _1ShBrl _3z3XZ9 pukiJQ _2iOIqx _2h_2_Y']")))    
    driver.find_element_by_xpath("//button[@class='_35rr5y _32qX4k _1ShBrl _3z3XZ9 pukiJQ _2iOIqx _2h_2_Y']").click()
 

def scroll_down_until_end(driver):
    """
    This function simply scrolls down the page until there is no more room to scroll.
    
    """
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Do it 5 times with delay to be sure.
        for i in range(0,5):
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def save_webpage(driver, file_name):

    html_contents = driver.page_source

    with open(file_name, "w") as f:
        f.write(html_contents)


def clear_screen():
    """
    Prints newline 100 times to behave like a clear screen.
    """
    print(100*"\n")
    os.system("clear")

def main():

    clear_screen()

    print(message)

    # Creates an option for how the browser behaves. 
    opts = Options()
    opts.headless = True
    #assert opts.headless   
    
    # Creates firefox webdriver.
    driver = Firefox(options=opts)

    # Navigate to the link provided.
    driver.get("https://shopee.ph/buyer/login")

    try:
        username_email = input("Enter your email address or username: ")
        password = getpass.getpass("Enter your password (it won't appear in the terminal): ")

        # Login to Shopee.
        if login(username_email, password, driver):
            
            # If login success, mobile verification is required.
            mobile_verification_number = input("Enter verification code sent in your mobile number: ")
            mobile_verification(mobile_verification_number, driver)

            # If mobile verification in success, the username navbar in the Shopee website should be present.
            # We wait for it to be present via div element with attribute name  "navbar__username" then we click it.
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='navbar__username']")))

            # If that is success, we navigate to purchase page.
            driver.get("https://shopee.ph/user/purchase/")

            # Perform scroll downs to load all puchased item so we can parse it.
            scroll_down_until_end(driver)

            # If the scroll is success, at this point we have now the page of Shopee with all the items
            # bought. We can scrape it.
            time.sleep(1)
            webpage_save_name = "webpage_contents.html"
            save_webpage(driver, webpage_save_name)

            item_info = scrape_webpage_contents.get_dict_items(webpage_save_name, username_email)
            #print(item_info_dict)

        
            file_title = "Summary of your Shopee Orders"
            date_generated = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

            file_name = "shopee-summary-" + date_generated.replace(" ", "-").replace("/","-").replace(":","-").replace(",","-") + ".pdf"
            file_name = os.path.join("generated_reports", file_name)

            file_description = "Account of: {}\nGenerated on: {}".format(username_email,date_generated)

        
            generate_report.generate_report_from_dict(file_name, file_title, file_description, item_info)

            print("PDF summary generated.")
        
         
        else:
            print("Invalid credentials.")

    except Exception as exp:
        
        print("An error has occured.")
        print(str(exp))

    finally:
        print("Program ended.")
        #input("Press enter to exit.")
        driver.close()


if __name__ == "__main__":
    main()