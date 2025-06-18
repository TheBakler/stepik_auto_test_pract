from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    value = browser.find_element(By.ID, "input_value")
    x_val = value.text
    res = calc(x_val)

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(res)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_robot.click()

    choice_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    choice_rule.click()


    push_sub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    push_sub.click()

finally:
    time.sleep(15)
    browser.quit()