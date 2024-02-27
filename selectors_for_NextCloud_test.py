from selenium.webdriver.common.by import By


class Login:
    username = (By.NAME, "user")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")


class FileSelectors:
    files_app_selector = (By.CSS_SELECTOR, "a[href='/apps/files/']")
    new_file_button = (By.CSS_SELECTOR, "span.button-vue__text")
    choose_file_type = (By.CSS_SELECTOR, "span.action-button__icon.icon-filetype-text")
    create_file = (By.CSS_SELECTOR, "input[type='submit'].primary")
    dots_menu_button = (By.XPATH, "//tr[.//span[text()='New text file']]//span[contains(@class, 'material-design-icon') and contains(@class, 'dots-horizontal-icon')]")
    delete_file_button = (By.CSS_SELECTOR, "li:nth-of-type(11) > button[role='menuitem']")
    new_file_locator = (By.XPATH, "//tr[.//span[text()='New text file']]")


# (By.CSS_SELECTOR, "span.material-design-icon.dots-horizontal-icon")

# button-vue__menu-toggle


'''.button-vue.button-vue--icon-only.button-vue--vue-tertiary.action"
                                    "-item__menutoggle'''