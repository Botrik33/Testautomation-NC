import time

from selenium import webdriver

from Tests.new_contact_user_model import NewContactUser
from Tests.test_skapa_conversation_model import MakeConversation


def test_new_contact_user():
    driver = webdriver.Chrome()
    new_contact_user = NewContactUser(driver)
    new_contact_user.open()
    new_contact_user.execute_login("_selenium_patryk", "patryk0406")
    new_contact_user.execute_test("Selenium User")
    assert "Selenium User" in driver.page_source
    driver.quit()


def test_skapa_conversation():
    driver = webdriver.Chrome()
    new_conversation = MakeConversation(driver)
    new_conversation.open()
    new_conversation.execute_login("_selenium_patryk", "patryk0406")
    new_conversation.execute_test("Selenium Conversation")
    assert "Selenium Conversation" in driver.page_source
