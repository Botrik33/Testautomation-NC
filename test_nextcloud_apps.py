import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_NextCloud_Apps:
    def test_nextcloud_apps(self, driver):
        driver.get("https://itsl.demo.hubs.se/apps/dashboard/")
        time.sleep(2)

        wait = WebDriverWait(driver, 10)

        login_username_locator = wait.until(EC.presence_of_element_located((By.NAME, "user")))
        login_username_locator.send_keys("_selenium_patryk")

        login_password_locator = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        login_password_locator.send_keys("patryk0406")

        login_submit_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_submit_button_locator.click()

        file_app_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/apps/files/']")))
        file_app_locator.click()
        file_url = driver.current_url
        expected_file_url = "https://itsl.demo.hubs.se/apps/files/?dir=/&fileid=5075"
        assert file_url == expected_file_url

        photos_app_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/apps/photos/']")))
        photos_app_locator.click()
        photos_url = driver.current_url
        expected_photos_url = "https://itsl.demo.hubs.se/apps/photos/"
        assert photos_url == expected_photos_url

        activity_app_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/apps/activity/']")))
        activity_app_locator.click()
        activity_url = driver.current_url
        expected_activity_url = "https://itsl.demo.hubs.se/apps/activity/"
        assert activity_url == expected_activity_url

        talk_app_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-app-id='spreed']")))
        talk_app_locator.click()
        talk_url = driver.current_url
        expected_talk_url = "https://itsl.demo.hubs.se/apps/spreed/"
        assert talk_url == expected_talk_url

        mail_app_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-app-id='mail']")))
        mail_app_locator.click()
        mail_url = driver.current_url
        expected_mail_url = "https://itsl.demo.hubs.se/apps/mail/box/priority"
        assert mail_url == expected_mail_url

        contacts_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/contacts/']")
        contacts_app_locator.click()
        contacts_url = driver.current_url
        expected_contacts_url = "https://itsl.demo.hubs.se/apps/contacts/All%20contacts"
        assert contacts_url == expected_contacts_url

        calendar_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/calendar/']")
        calendar_app_locator.click()
        calendar_url = driver.current_url
        expected_calendar_url = "https://itsl.demo.hubs.se/apps/calendar/dayGridMonth/now"
        assert calendar_url == expected_calendar_url

        notes_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/notes/']")
        notes_app_locator.click()
        notes_url = driver.current_url
        expected_notes_url = "https://itsl.demo.hubs.se/apps/notes/welcome"
        assert notes_url == expected_notes_url

        deck_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/deck/']")
        deck_app_locator.click()
        deck_url = driver.current_url
        expected_deck_url = "https://itsl.demo.hubs.se/apps/deck/#/"
        assert deck_url == expected_deck_url

        collectives_app_locator = driver.find_element(By.CSS_SELECTOR, "a[href='/apps/collectives/']")
        collectives_app_locator.click()
        collectives_url = driver.current_url
        expected_collectives_url = "https://itsl.demo.hubs.se/apps/collectives/"
        assert collectives_url == expected_collectives_url

