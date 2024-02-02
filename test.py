from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':
    service = Service(executable_path= "/Desktop/Drivers/chromedriver.exe")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    chromeOptions.add_argument('--log-level=3')
    # chromeOptions.add_argument('--headless')
    # chromeOptions.add_argument('--no-sandbox')
    # chromeOptions.add_argument('--disable-dev-shm-usage')
   
    
    driver = webdriver.Chrome(service=service, options=chromeOptions)
    driver.set_window_size(1920, 1080)
  
    driver.get('https://www.geeksforgeeks.org/')
    time.sleep(60)
    driver.quit()
    print("Done")
