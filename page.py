from locators import MainPageLocators
from locators import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "query"

class UsernameTextElement(BasePageElement):
    locator = "username"

class PasswordTextElement(BasePageElement):
    locator = "password"


class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()
    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()
    
    def is_title_matches(self):
        return "osu!" in self.driver.title
    
    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def click_username_input(self):
        element = self.driver.find_element(*MainPageLocators.USERNAME_INPUT)
        element.click()

    def click_password_input(self):
        element = self.driver.find_element(*MainPageLocators.PASSWORD_INPUT)
        element.click()

    def click_connect_button(self):
        element = self.driver.find_element(*MainPageLocators.CONNECT_BUTTON)
        element.click()

class SearchResultPage(BasePage):
    
    def is_result_found(self):
        return "No results found." not in self.driver.page_source

class LoginResultPage(BasePage):

    def is_login_successful(self):
        return "Login incorreto" not in self.driver.page_source