from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
import message_generator

config = configparser.ConfigParser()
config.read('config.ini', 'utf-8')

user_config = config['User']
details_config = config['Details']

email = user_config.get('EMAIL')
password = user_config.get('PASSWORD')
teacher = details_config.get('TEACHER')
if details_config.get('is_auto_generated') == "False":
    message = details_config.get('MESSAGE')
else:
    message = message_generator.generate_message()

print('Email:', email)
print('Password:', password)
print('Teacher:', teacher)
print('Message:', message)

def wait_element_clickable(driver, locator, timeout=100):
    """Waits for an element to be clickable and returns it."""
    print(f"Waiting for element to be clickable: {locator}")
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
    print(f"Element is clickable: {locator}")
    return driver.find_element(By.XPATH, locator)

def main():
    print("Starting the Selenium WebDriver...")
    with webdriver.Chrome() as driver:
        print("Opening Microsoft Teams login page...")
        driver.get("https://www.microsoft.com/pl-pl/microsoft-teams/log-in")

        print("Clicking on the login link...")
        wait_element_clickable(driver, "//a[@aria-label='Zaloguj się do usługi Microsoft Teams']").click()

        time.sleep(1)

        print("Waiting for new window to open...")
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        print("Switching to the new window...")
        driver.switch_to.window(driver.window_handles[1])

        time.sleep(1)

        print("Waiting for the login input field...")
        login = wait_element_clickable(driver, "//input[@name='loginfmt']")
        print("Entering email...")
        login.send_keys(email, Keys.ENTER)

        time.sleep(1)

        print("Waiting for the password input field...")
        pswd = wait_element_clickable(driver, "//input[@name='passwd']")
        print("Entering password...")
        pswd.send_keys(password, Keys.ENTER)

        time.sleep(1)

        print("Waiting for the submit button...")
        submit = wait_element_clickable(driver, "//input[@type='submit' and @id='idSIButton9']")
        print("Clicking submit button...")
        submit.click()

        time.sleep(1)

        print("Waiting for the search input field...")
        search = wait_element_clickable(driver, "//input[@id='ms-searchux-input']")
        print(f"Searching for teacher: {teacher}...")
        search.send_keys(teacher, Keys.ENTER)

        time.sleep(1)

        print("Waiting for the 'People' button...")
        people = wait_element_clickable(driver, "//button[@value='people']")
        print("Clicking on 'People' button...")
        people.click()

        time.sleep(1)

        print("Waiting for the teacher account element...")
        teacher_acc = wait_element_clickable(driver, "//li[@aria-posinset='0']")
        print("Clicking on the teacher account...")
        teacher_acc.click()

        time.sleep(1)

        print("Waiting for the message box...")
        message_box = wait_element_clickable(driver, "//div[contains(@id, 'new-message')]")
        print(f"Sending message: {message}...")
        message_box.send_keys(message, Keys.ENTER)

        print("Message sent. Waiting before closing...")
        time.sleep(2)
    
    print("Finished execution.")

if __name__ == "__main__":
    main()
