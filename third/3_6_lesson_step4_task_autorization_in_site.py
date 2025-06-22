from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

class TestMainPage():


    @pytest.mark.parametrize("links", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_autorization(self, browser, load_config, links):

        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        time.sleep(10)
        login = load_config["login_stepik"]
        password = load_config["password_stepik"]

        browser.find_element(By.ID, "ember479").click()

        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys(login)

        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys(password)


        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        #time.sleep(7)
        input3 = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        #input3 = browser.find_element(By.TAG_NAME, "textarea")
        answer = str(math.log(int(time.time())))
        input3.send_keys(answer)

        #wait.until(browser.find_element(By.CSS_SELECTOR, "button.submit-submission")).click()
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()

        #time.sleep(5)
        message = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
        #message = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        print(message)
        assert message == "Correct!"

if __name__ == "__main__":
    pytest.main()





