import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNextCloudConversation:
    def test_nextcloud_conversation(self, driver):
        driver.get("https://itsl.demo.hubs.se/apps/dashboard/")

        wait = WebDriverWait(driver, 10)

        login_username_locator = wait.until(EC.presence_of_element_located((By.NAME, "user")))
        login_username_locator.send_keys("_selenium_patryk")

        login_password_locator = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        login_password_locator.send_keys("patryk0406")

        login_submit_button_locator = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        login_submit_button_locator.click()

        talk_app_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-app-id='spreed']")))
        talk_app_locator.click()

        make_conversation_button_locator = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".action-item.action-item--tertiary.actions")))

        make_conversation_button_locator.click()

        create_conversation_locator = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[@class='action-button__longtext' and text()='Create a new conversation']")))

        create_conversation_locator.click()

        conversation_name_locator = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter a name for this conversation']")))

        conversation_name_locator.send_keys("Selenium Conversation")

        add_participants_locator = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                              "//span[@class='button-vue__text' and text()='Add participants']")))
        add_participants_locator.click()


        add_participants_locator = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search participants']")))
        driver.execute_script("arguments[0].value='patryk';", add_participants_locator)


        input_value = add_participants_locator.get_attribute('value')
        assert input_value == "patryk"

        add_user_to_conversation = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='patryk@itsl.se']")))
        add_user_to_conversation.click()

        create_conversation_button_locator = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='button-vue__text' and text()='Create conversation']")))
        create_conversation_button_locator.click()

        new_conversation_locator = (
            By.XPATH, "//span[@class='line-one__title' and contains(text(), 'Selenium Conversation')]")
        new_conversation_element = wait.until(EC.presence_of_element_located(new_conversation_locator))

        ActionChains(driver).move_to_element(new_conversation_element).perform()

        kebab_menu_locator = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Conversation actions']")))
        kebab_menu_locator.click()

        delete_conversation_locator = wait.until(element_to_be_clickable(
            (By.XPATH, "//span[@class='action-button__text' and contains(text(), 'Delete conversation')]")))
        delete_conversation_locator.click()

        yes_button_locator = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='primary' and text()='Yes']")))
        yes_button_locator.click()
        assert EC.invisibility_of_element_located(new_conversation_locator)

