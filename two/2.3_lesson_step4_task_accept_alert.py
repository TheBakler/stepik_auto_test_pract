from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    push_next = browser.find_element(By.CSS_SELECTOR, "button.btn")
    push_next.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    find_num_x = browser.find_element(By.ID, "input_value")
    x_el = find_num_x.text
    summary = calc(x_el)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(summary)

    push_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    push_submit.click()


finally:
    time.sleep(15)
    browser.quit()