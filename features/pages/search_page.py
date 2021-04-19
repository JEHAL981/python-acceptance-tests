from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    # Web elements on Main Page
    LOGO = (By.ID, 'nav-logo-sprites')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, '.sg-col-inner')

    def __init__(self, driver):
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.SEARCH).send_keys(item)
        self.find_element(*self.SEARCH).send_keys(Keys.ENTER)

    def get_search_result(self):
        return self.find_element(*self.SEARCH_LIST).text
