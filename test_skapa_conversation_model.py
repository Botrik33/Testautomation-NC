from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MakeConversation:
    __url = "https://itsl.demo.hubs.se/apps/dashboard/"
    __username_field = (By.NAME, "user")
    __password_field = (By.NAME, "password")
    __login_button = (By.XPATH, "//button[@type='submit']")
    __talk_app = (By.CSS_SELECTOR, "li[data-app-id='spreed']")
    __make_conversation_button = (By.CSS_SELECTOR, ".action-item.action-item--tertiary.actions")
    __create_conversation = (By.XPATH, "//p[@class='action-button__longtext' and text()='Create a new conversation']")
    __conversation_name = (By.XPATH, "//input[@placeholder='Enter a name for this conversation']")
    __add_participants = (By.XPATH, "//span[@class='button-vue__text' and text()='Add participants']")
    __search_participants = (By.XPATH, "//input[@placeholder='Search participants']")
    __add_user_to_conversation = (By.XPATH, "//span[text()='patryk@itsl.se']")
    __create_conversation_button = (By.XPATH, "//span[@class='button-vue__text' and text()='Create conversation']")
    __new_conversation = (By.XPATH, "//span[text()='Selenium Conversation']")
    __kebab_menu = (By.CSS_SELECTOR, "[aria-label='Conversation actions']")
    __delete_conversation = (By.XPATH, "//span[@class='action-button__text' and contains(text(), 'Delete conversation')]")
    __yes_button = (By.XPATH, "//span[@class='button-vue__text' and text()='Yes']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        self._driver.find_element(*self.__username_field).send_keys(username)
        self._driver.find_element(*self.__password_field).send_keys(password)
        self._driver.find_element(*self.__login_button).click()

    def execute_test(self, selenium_conversation: str):

        self._driver.find_element(*self.__talk_app).click()
        self._driver.find_element(*self.__make_conversation_button).click()
        self._driver.find_element(*self.__create_conversation).click()
        self._driver.find_element(*self.__conversation_name).send_keys(selenium_conversation)
        self._driver.find_element(*self.__add_participants).click()
        search_participants_locator = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(self.__search_participants))
        self._driver.execute_script("arguments[0].value='patryk';", search_participants_locator)
        self._driver.find_element(*self.__add_user_to_conversation).click()
        self._driver.find_element(*self.__create_conversation_button).click()
        self._driver.find_element(*self.__new_conversation).click()
        self._driver.find_element(*self.__kebab_menu).click()
        self._driver.find_element(*self.__delete_conversation).click()
        self._driver.find_element(*self.__yes_button).click()
