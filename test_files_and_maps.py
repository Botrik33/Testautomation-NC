import time

import yaml
import os
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import xmlrunner

from test_chris_patryk.NextCloudTestCase import NextCloudTestCase
from test_chris_patryk.selectors_for_NextCloud_test import FileSelectors


class FileAndMapsTests(NextCloudTestCase):

    def test_files(self):
        wait = WebDriverWait(self.driver, 10)
        self.navigate_to_file_app()
        self.make_new_file()
        self.delete_file()
        success_message = wait.until(EC.visibility_of_element_located(FileSelectors.toast_message))
        self.assertTrue(success_message.is_displayed(), 'Success message should be displayed after file deletion')

    def test_maps(self):
        wait = WebDriverWait(self.driver, 10)
        self.navigate_to_file_app()
        try:
            self.make_maps_file()
        finally:
            self.delete_maps()
        maps_success_message = wait.until(EC.visibility_of_element_located(FileSelectors.toast_message))
        self.assertTrue(maps_success_message.is_displayed(), 'Success message should be displayed after maps file deletion')












