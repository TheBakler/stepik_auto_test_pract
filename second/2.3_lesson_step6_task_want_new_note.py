from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    push_trollface = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    push_trollface.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    find_num = browser.find_element(By.ID, "input_value")
    x_el = find_num.text
    summary = calc(x_el)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(summary)

    push_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    push_submit.click()

finally:
    time.sleep(15)
    browser.quit()