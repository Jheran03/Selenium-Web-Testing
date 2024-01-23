import unittest
import page
import time
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import find_dotenv, load_dotenv

service = Service(executable_path="chromedriver.exe")

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

login_username = os.getenv("ID")
login_password = os.getenv("PASSWORD")

class OsuSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://osu.ppy.sh/home/search")

    def test_title(self):
        main_page= page.MainPage(self.driver)
        assert main_page.is_title_matches()

    def test_search_query(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "owc"
        search_results_page = page.SearchResultPage(self.driver)
        self.assertTrue(search_results_page.is_result_found(),"No results found.")

    def test_login(self):
        main_page= page.MainPage(self.driver)
        main_page.click_login_button()
        main_page.click_username_input()
        main_page.username_text_element = login_username
        main_page.click_password_input()
        main_page.password_text_element = login_password
        main_page.click_connect_button()
        login_result_page = page.LoginResultPage(self.driver)
        time.sleep(1)
        self.assertTrue(login_result_page.is_login_successful(), "Login incorreto")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()