from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num_find_one = browser.find_element(By.ID, "num1")
    x_el = num_find_one.text

    num_find_two = browser.find_element(By.ID, "num2")
    y_el = num_find_two.text

    sum = str(int(x_el) + int(y_el))

    ans_num = Select(browser.find_element(By.TAG_NAME, "select"))
    ans_num.select_by_value(sum)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()




