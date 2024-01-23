from selenium.webdriver.common.by import By

class MainPageLocators(object):
    
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div[2]/div[4]/button")
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    CONNECT_BUTTON = (By.XPATH, "/html/body/div[5]/div/form/div[5]/div/button")

class SearchResultsPageLocators(object):
    pass