import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "./chromedriver.exe"
URL = "https://play.typeracer.com/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH), options=options)
driver.get(URL)
sentence = ""

try:
    # Grab practice button. I ONLY DOING THIS IN PRACTICE MODE - I AINT A SCUMBAG. Unless........<.<
    practice_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-2"]/a')))
    practice_btn.click()
    # Grab text box
    text = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')))
    span_list = text.find_elements(By.TAG_NAME, "span")
    for span in span_list:
        sentence+=span.get_attribute("innerHTML") # Doing "span.text" no workie so I do "get_attribute" instead...
except Exception as e:
    print(e)
sleep(4.5) # give me some to pick the window cuh
pyautogui.typewrite(sentence, interval=0.025)
