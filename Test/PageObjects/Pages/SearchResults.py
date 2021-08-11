from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.PageObjects.Locators.SearchResults import Locator
from Test.TestUtils import Utils as UT


class SearchResults(object):

    def __init__(self, driver, search_value):
        self.driver = driver
        searched_item = UT.format_xpath(Locator.header_results_for_searched_item, search_value)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, searched_item)))

    def select_page_by_number(self, number):
        button_page = UT.format_xpath(Locator.button_page, number)
        button_page = self.driver.find_element(By.XPATH, button_page)
        button_page.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes)

    def select_item_by_index(self, index):
        product_by_index = UT.format_xpath(Locator.product_by_index, index)
        product_by_index = self.driver.find_element(By.XPATH, product_by_index)
        product_by_index.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes)
