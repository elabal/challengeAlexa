import unittest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Test.TestUtils import Utils as UT


class EnvSetUp(unittest.TestCase):
    def setUp(self):
        self.test_failed = True
        """Setting test_failed flag"""
        print("Environment Set Up")
        browser = UT.get_param("browser")

        """Setup for firefox or chrome, and capabilities"""
        if browser == 'firefox':
            print("///Opening Firefox///")
            options = FirefoxOptions()
            if UT.get_param("headless") == "true":
                print("///Headless mode enabled///")
                options.add_argument("--headless")
            else:
                print("///Headless mode disabled///")
            options.log.level = "trace"
            self.driver = webdriver.Firefox(options=options)
            self.driver.maximize_window()

        elif browser == 'chrome':
            print("///Opening Chrome///")
            options = ChromeOptions()
            if UT.get_param("headless") == "true":
                print("///Headless mode enabled///")
                options.add_argument("--headless")
                options.add_argument("--window-size=1325x744")
            else:
                print("///Headless mode disabled///")
            d = DesiredCapabilities.CHROME
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=d)
            self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        print("Running test " + self._testMethodName)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("Run started at : " + str(datetime.now()))
        print("----------------------------------------------------------------------------------------------------------------------------------------")

    def tearDown(self):
        if self.test_failed:
            print("EXECUTION FAILED AT: " + self.driver.current_url)
            UT.get_screenshot(self.driver)
        print("Run finished at : " + str(datetime.now()))
        self.driver.close()
        self.driver.quit()
        print("----------------------------------------------------------------------------------------------------------------------------------------")
