import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestNewContactsUser:
    def test_new_contacts_user(self, driver):
        driver.get("https://itsl.demo.hubs.se/apps/dashboard/")
        time.sleep(2)

        wait = WebDriverWait(driver, 10)

        login_username_locator = wait.until(EC.presence_of_element_located((By.NAME, "user")))
        login_username_locator.send_keys("_selenium_patryk")

        login_password_locator = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        login_password_locator.send_keys("patryk0406")

        login_submit_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_submit_button_locator.click()

        contacts_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/contacts/']")
        contacts_app_locator.click()

        new_contact_button_locator = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'New contact')]")))
        new_contact_button_locator.click()

        name_input_locator = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='contact-fullname']")))

        name_input_locator.clear()

        name_input_locator.send_keys("Selenium Patryk")

        save_user_element_locator = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".contact-header__actions .button-vue--vue-secondary .button-vue__icon")))

        assert save_user_element_locator.is_displayed() == True
        save_user_element_locator.click()
