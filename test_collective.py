import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNextCloudConversation:
    def test_nextcloud_conversation(self, driver):
        driver.get("https://itsl.demo.hubs.se/apps/dashboard/")
        time.sleep(2)

        wait = WebDriverWait(driver, 10)

        login_username_locator = wait.until(EC.presence_of_element_located((By.NAME, "user")))
        login_username_locator.send_keys("_selenium_patryk")

        login_password_locator = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        login_password_locator.send_keys("patryk0406")

        login_submit_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_submit_button_locator.click()

        collectives_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/collectives/']")
        collectives_app_locator.click()

        collective_button_locator = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                               "//button[@class='button-vue button-vue--text-only button-vue--vue-primary' and @aria-label='Create new collective']")))
        collective_button_locator.click()

        collective_name_locator = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name of the collective']")))
        collective_name_locator.send_keys("Selenium Collective")
        assert collective_name_locator.get_attribute("value") == "Selenium Collective"

        add_members_button_locator = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='button-vue__text' and text()='Add members']")))
        add_members_button_locator.click()

        add_members_name_locator = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@placeholder, 'Search accounts, groups, circles')]")))
        add_members_name_locator.send_keys("Welat")
        assert add_members_name_locator.get_attribute("value") == "Welat"

        user_name_locator = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='member-row__user-name' and text()='Welat Cengiz']")))
        user_name_locator.click()

        add_user_locator = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='button-vue__text' and text()='Create']")))
        add_user_locator.click()

        kebab_menu_locator = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "li.app-navigation-entry__wrapper .app-navigation-entry__actions .action-item--tertiary button[aria-label='Actions']")))
        kebab_menu_locator.click()

# .v-popper.v-popper--shown.v-popper--theme-dropdown > .action-item__menutoggle.button-vue.button-vue--icon-only.button-vue--vue-tertiary span[role='img'] > .material-design-icon__svg > path
