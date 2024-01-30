from selenium.webdriver.common.by import By


class NewTablesModel:
    __url = "https://itsl.demo.hubs.se/apps/dashboard/"
    __username_field = (By.NAME, "user")
    __password_field = (By.NAME, "password")
    __login_button = (By.XPATH, "//button[@type='submit']")

