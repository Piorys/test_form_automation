import unittest
from selenium import webdriver

targetSite = "http://executeautomation.com/demosite/index.html"


class FormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_form_basic(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(targetSite)

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
        gender_female_check = driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[5]/td[2]/input[2]')
        gender_female_check.click()

        # Step
        known_languages_hindi = driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[6]/td[2]/input[2]')
        known_languages_hindi.click()

        # Step
        known_languages_english = driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[6]/td[2]/input[1]')
        known_languages_english.click()

        # Step
        save_btn = driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[7]/td/input')
        save_btn.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
