from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Artemy")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Nosov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("artemiiiiiii.nosov@vip.com")


    input_file = browser.find_element(By.ID, "file")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    input_file.send_keys(file_path)

    push_sub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    push_sub.click()


finally:
    time.sleep(15)
    browser.quit()