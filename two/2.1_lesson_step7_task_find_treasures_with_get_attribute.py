import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x_el = x_element.get_attribute("valuex")
    y = calc(x_el)

    input_value = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_value.send_keys(y)

    check_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_robot.click()

    choice_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    choice_rule.click()

    push_sub = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    push_sub.click()


finally:
    time.sleep(30)
    browser.quit()