import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)
        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(4)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"
        # Verify error message text is Your password is invalid!
        error_message_locator = error_message_locator.text
        assert error_message_locator == expected_error_message

    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("studentt")
        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(2)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"
        # Verify error message text is Your password is invalid!
        error_message_locator = error_message_locator.text
        assert error_message_locator == "Your username is invalid!"


class TestNegativePassword:

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password1234")
        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button.click()
        time.sleep(2)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed()

        error_message_locator = error_message_locator.text
        # Verify error message text is Your password is invalid!
        assert error_message_locator == "Your password is invalid!"
