from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "Alan Goźliński"
EMAIL = "agozlinski352@technikumkreatywne.pl"
PASSWORD = "(GoldenExpRequiem12#118)"
TEACHER = "Jacek Konczalski"
MESSAGE = "JKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKJK"  

def wait_element_clickable(driver, locator, timeout=20):
    """Waits for an element to be clickable and returns it."""
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
    return driver.find_element(By.XPATH, locator)

def main():
    with webdriver.Chrome() as driver:
        driver.get("https://www.microsoft.com/pl-pl/microsoft-teams/log-in")

        wait_element_clickable(driver, "//a[@aria-label='Zaloguj się do usługi Microsoft Teams']").click()

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        login = wait_element_clickable(driver, "//input[@name='loginfmt']")
        login.send_keys(EMAIL, Keys.ENTER)

        password = wait_element_clickable(driver, "//input[@name='passwd']")
        password.send_keys(PASSWORD, Keys.ENTER)

        wait_element_clickable(driver, "//input[@type='submit' and @id='idSIButton9']").click()

        search = wait_element_clickable(driver, "//input[@id='ms-searchux-input']")
        search.send_keys(TEACHER, Keys.ENTER)

        wait_element_clickable(driver, "//button[@value='people']").click()

        wait_element_clickable(driver, "//li[@aria-posinset='0']").click()

        message_box = wait_element_clickable(driver, "//div[contains(@id, 'new-message')]")
        message_box.send_keys(MESSAGE, Keys.ENTER)

        time.sleep(2)

if __name__ == "__main__":
    main()
