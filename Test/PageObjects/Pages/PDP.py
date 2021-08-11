from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.PageObjects.Locators.PDP import Locator


class PDP(object):

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locator.ppd_container)))

    def check_available_for_purchase(self):
        assert self.driver.find_element(Locator.add_to_cart) in self.driver

