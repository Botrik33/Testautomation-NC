import time
import unittest

import xmlrunner
import yaml
import os
import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from test_chris_patryk.selectors_for_NextCloud_test import FileSelectors, Login, MapsSelector


class NextCloudTestCase(unittest.TestCase):

    def setUp(self):
        with open('/Users/patrykkowalski/PycharmProjects/Learn_Automation/test_chris_patryk/expected.yaml') as file:
            self.expected_data = yaml.safe_load(file)

        self.env_to_test = os.getenv('TEST_ENVIRONMENT')
        self.env_config = self.expected_data.get(self.env_to_test, {})
        self.url = os.getenv('TEST_URL')
        self.username = os.getenv('SELENIUM_USERNAME')
        self.password = os.getenv('SELENIUM_PASSWORD')

        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.chrome_options)

        logging.info(f'testing against environment: {self.env_to_test}')
        logging.info(f'testing against url: {self.url}')

        self.driver.get(self.url + '/login')
        # cls.driver.find_element(By.XPATH, "//div[@class='login-option'][1]").click()

        self.driver.find_element(*Login.username).send_keys(self.username)
        self.driver.find_element(*Login.password).send_keys(self.password)
        self.driver.find_element(*Login.login_button).click()

    def navigate_to_file_app(self):
        logging.info('Navigating to the files app')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(FileSelectors.files_app_selector)).click()

    def make_new_file(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            logging.info('Clicking on new button')
            wait.until(EC.element_to_be_clickable(FileSelectors.new_file_button)).click()
            logging.info('Choosing file type')
            wait.until(EC.element_to_be_clickable(FileSelectors.choose_file_type)).click()
            logging.info('Creating new file')
            wait.until(EC.element_to_be_clickable(FileSelectors.create_file)).click()
        except TimeoutException:
            logging.error('Failed to create new file')
            self.driver.save_screenshot("NewFileError.png")
            raise

    def delete_file(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            logging.info('Refreshing the page')
            self.driver.refresh()
            logging.info('Clicking on the dots menu')
            wait.until(EC.element_to_be_clickable(FileSelectors.dots_menu_button)).click()
            logging.info('Clicking on the delete file button')
            wait.until(EC.element_to_be_clickable(FileSelectors.delete_file_button)).click()
        except TimeoutException:
            logging.error('Failed to delete file')
            self.driver.save_screenshot("DeleteFileError.png")
            raise

    def make_maps_file(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            logging.info('Clicking on new button')
            wait.until(EC.element_to_be_clickable(FileSelectors.new_file_button)).click()
            logging.info('Choosing maps')
            wait.until(EC.element_to_be_clickable(MapsSelector.choose_maps)).click()
            logging.info('Creating new maps file')
            wait.until(EC.element_to_be_clickable(FileSelectors.create_file)).click()
        except TimeoutException:
            logging.warning('TimeoutException caught. Continuing test despite error')

    def delete_maps(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            logging.info('Refreshing the page')
            self.driver.refresh()
            logging.info('Clicking on the dots menu')
            wait.until(EC.element_to_be_clickable(MapsSelector.dots_menu_button_maps)).click()
            logging.info('Clicking on the delete file button')
            wait.until(EC.element_to_be_clickable(MapsSelector.delete_maps_button)).click()
        except TimeoutException:
            logging.error('Failed to delete maps file')
            self.driver.save_screenshot("DeleteMapsFileError.png")
            raise

    def tearDown(self):
        logging.info('Starting teardown process...')
        if hasattr(self, 'driver'):
            try:
                self.driver.delete_all_cookies()
                self.driver.quit()
                logging.info('WebDriver session successfully closed')
            except Exception as e:
                logging.error(f'An error occurred while closing the WebDriver session: {e}')
        else:
            logging.warning('WebDriver session was not properly initialized')
        logging.info('Teardown process finished')


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))
