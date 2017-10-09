import unittest
from selenium import webdriver

targetSite = "http://executeautomation.com/demosite/index.html"


class PopUpTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_jsPopup_basic(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(targetSite)
    # Step
        popup_btn = driver.find_element_by_xpath('//*[@id="details"]/div[2]/p/input')
        popup_btn.click()
    # Step
        alert = driver.switch_to_alert()
        alert.accept()
    # Step
        alert_1 = driver.switch_to_alert()
        alert_1.accept()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()
