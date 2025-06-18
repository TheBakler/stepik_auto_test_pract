from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class Test(unittest.TestCase):
    def test_registration_one(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input3.send_keys("ivan.petrov@mail.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your phone:']")
        input4.send_keys("89304567892")
        input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your address:']")
        input5.send_keys("Moscow")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        WebDriverWait(browser, 1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration_two(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
        input3.send_keys("ivan.petrov@mail.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your phone:']")
        input4.send_keys("89304567892")
        input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your address:']")
        input5.send_keys("Moscow")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        WebDriverWait(browser, 1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()