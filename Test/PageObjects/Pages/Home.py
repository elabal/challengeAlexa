from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.PageObjects.Locators.Home import Locator


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.amazon_logo)))
        self.search_box = driver.find_element(By.XPATH, Locator.search_box)
        self.submit_search = driver.find_element(By.XPATH, Locator.submit_search)

    def search_item_by_name(self, item):
        self.search_box.send_keys(item)
        self.submit_search.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes)

