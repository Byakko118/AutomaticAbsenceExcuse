from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "Alan Goźliński"
EMAIL = "agozlinski352@technikumkreatywne.pl"
PASSWORD = "(GoldenExpRequiem12#118)"
TEACHER = "Jacek Konczalski"  # This can be changed later

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(25)
    driver.get("https://www.microsoft.com/pl-pl/microsoft-teams/log-in")

    # Log in
    login = driver.find_element(By.CLASS_NAME, "btn ")
    login.click()

    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "loginfmt")))
    email_input.send_keys(EMAIL)

    next_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    next_btn.click()

    pswd_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "passwd")))
    pswd_input.send_keys(PASSWORD)

    finish_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    finish_btn.click()

    yes_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    yes_btn.click()

    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ms-searchux-input")))
    search.send_keys(TEACHER)
    search.send_keys(Keys.ENTER)

    people = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='people']")))
    people.click()

    time.sleep(10)  

    driver.quit()

if __name__ == "__main__":
    main()
