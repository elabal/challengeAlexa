import sys
sys.path.append(sys.path[0] + "/....")
import os
sys.path.append(os.getcwd())
import unittest
from Test.TestBase.EnvSetUp import EnvSetUp
from Test.TestUtils import Utils as UT
from Test.PageObjects.Pages.Home import Home
from Test.PageObjects.Pages.SearchResults import SearchResults
from Test.PageObjects.Pages.PDP import PDP


class TestAssertCart(EnvSetUp):

    def test_assert_cart(self):
        driver = self.driver
        driver.get(UT.get_param("base_url"))

        home = Home(driver)
        home.search_item_by_name("Alexa")

        search_results = SearchResults(driver, "Alexa")
        search_results.select_page_by_number("2")
        search_results.select_item_by_index("3")

        pdp = PDP(driver)
        pdp.check_available_for_purchase()

        self.test_failed = False


if __name__ == "__main__":
    unittest.main()

