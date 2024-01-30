from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewContactUser:
    __url = "https://itsl.demo.hubs.se/apps/dashboard/"
    __username_field = (By.NAME, "user")
    __password_field = (By.NAME, "password")
    __login_button = (By.XPATH, "//button[@type='submit']")
    __contacts_app = (By.CSS_SELECTOR, "a[href='/apps/contacts/']")
    __new_contact_button = (By.XPATH, "//button[contains(., 'New contact')]")
    __name_input = (By.XPATH, "//input[@id='contact-fullname']")
    __save_user_element = (By.CSS_SELECTOR, ".contact-header__actions .button-vue--vue-secondary .button-vue__icon")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        self._driver.find_element(*self.__username_field).send_keys(username)
        self._driver.find_element(*self.__password_field).send_keys(password)
        self._driver.find_element(*self.__login_button).click()

    def execute_test(self, selenium_name: str):
        self._driver.find_element(*self.__contacts_app).click()
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.element_to_be_clickable(self.__new_contact_button)).click()
        self._driver.find_element(*self.__name_input).clear()
        wait.until(EC.presence_of_element_located(self.__name_input)).send_keys(selenium_name)
        self._driver.find_element(*self.__save_user_element).click()
