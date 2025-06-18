from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(By.ID, "book")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button.click()

find_num = browser.find_element(By.ID, "input_value")
x_el = find_num.text
summary = calc(x_el)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(summary)

push_submit = browser.find_element(By.ID, "solve")
push_submit.click()


time.sleep(5)
browser.quit()