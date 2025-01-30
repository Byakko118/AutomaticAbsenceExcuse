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
MESSAGE = "Niech pan obleje jarosława gałeckiego proszę bo on nic nie robi na lekcjach męczy mnie i takie tam gadanie XDDDDDDDDDDDDDDDDDD"

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(25)
    driver.get("https://www.microsoft.com/pl-pl/microsoft-teams/log-in")

    login = driver.find_element(By.CLASS_NAME, "btn ")
    login.click()

    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    email_input = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.NAME, "loginfmt")))
    email_input.send_keys(EMAIL)

    next_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    next_btn.click()

    pswd_input = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.NAME, "passwd")))
    pswd_input.send_keys(PASSWORD)

    finish_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    finish_btn.click()

    yes_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    yes_btn.click()

    search = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "ms-searchux-input")))
    search.send_keys(TEACHER)
    search.send_keys(Keys.ENTER)

    people = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[value='people']")))
    people.click()

    li_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//li[@aria-posinset='0']")))
    li_element.click()

    chat = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Wpisz wiadomość']")))
    chat.send_keys(f"{MESSAGE}")
    chat.send_keys(Keys.RETURN)

    time.sleep(2)  

    driver.quit()

if __name__ == "__main__":
    main()
