import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetSite = "http://executeautomation.com/demosite/index.html"


class FormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_form_popup_basic(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(targetSite)

    # Step
        popup_link = driver.find_element_by_xpath('//*[@id="details"]/div[1]/p/a')
        popup_link.click()

    # Step
        driver.switch_to.window("Popup")

    # Step
        tittle_dropdown = driver.find_element_by_id("TitleId")
        for option in tittle_dropdown.find_elements_by_tag_name("option"):
            if option == "Ms.":
                option.click()
                break
    # Step
        initial = driver.find_element_by_id("Initial")
        initial.send_keys("LI")

    # Step
        first_name = driver.find_element_by_id("FirstName")
        first_name.send_keys("Lorem")

    # Step
        middle_name = driver.find_element_by_id("MiddleName")
        middle_name.send_keys("Ipsum")

    # Step
        last_name = driver.find_element_by_id("LastName")
        last_name.send_keys("Dolor")

    # Step
        radio_gender_female = driver.find_element_by_xpath('//*[@id="popup"]/div[11]/span/input[2]')
        radio_gender_female.click()

    # Step
        country_dropdown = driver.find_element_by_id("Country")
        for option in tittle_dropdown.find_elements_by_tag_name("option"):
            if option == "Singapore":
                option.click()
                break
    # Step
        save_btn = driver.find_element_by_xpath('//*[@id="popup"]/div[15]/input')
        save_btn.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()