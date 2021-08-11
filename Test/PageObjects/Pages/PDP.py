from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.PageObjects.Locators.PDP import Locator
from selenium.common.exceptions import InvalidArgumentException


class PDP(object):

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locator.ppd_container)))

    def check_available_for_purchase(self):
        try:
            add_to_cart = self.driver.find_element(Locator.add_to_cart)
            add_to_cart.click()
        except InvalidArgumentException:
            raise Exception("Item is not avaiable for purchase")

