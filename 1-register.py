# added readings:
# - https://copyprogramming.com/howto/get-the-text-of-an-element-selenium-python
# - https://gist.github.com/devinmancuso/54904c005f8d237f6fec

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.data import data_used
from pageObject.locator import locator_used

class register_cases(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com"

    def test_a_empty_field_all(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.firstname_empty)))
        firstname_empty = driver.find_element(By.CSS_SELECTOR, locator_used.firstname_empty)
        self.assertIn(data_used.firstname_empty, firstname_empty.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.lastname_empty)))
        lastname_empty = driver.find_element(By.CSS_SELECTOR, locator_used.lastname_empty)
        self.assertIn(data_used.lastname_empty, lastname_empty.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.email_empty)))
        email_empty = driver.find_element(By.CSS_SELECTOR, locator_used.email_empty)
        self.assertIn(data_used.email_empty, email_empty.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.password_empty)))
        password_empty = driver.find_element(By.CSS_SELECTOR, locator_used.password_empty)
        self.assertIn(data_used.password_empty, password_empty.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.confpass_empty)))
        confpass_empty = driver.find_element(By.CSS_SELECTOR, locator_used.confpass_empty)
        self.assertIn(data_used.confpass_empty, confpass_empty.get_attribute("innerText"))

    def test_b_empty_field_firstname(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_used)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.firstname_empty)))
        firstname_empty = driver.find_element(By.CSS_SELECTOR, locator_used.firstname_empty)
        self.assertIn(data_used.firstname_empty, firstname_empty.get_attribute("innerText"))

    def test_c_empty_field_lastname(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_used)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.lastname_empty)))
        lastname_empty = driver.find_element(By.CSS_SELECTOR, locator_used.lastname_empty)
        self.assertIn(data_used.lastname_empty, lastname_empty.get_attribute("innerText"))

    def test_d_empty_field_email(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.email_empty)))
        email_empty = driver.find_element(By.CSS_SELECTOR, locator_used.email_empty)
        self.assertIn(data_used.email_empty, email_empty.get_attribute("innerText"))

    def test_e_empty_field_pass(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.new_email)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.password_empty)))
        password_empty = driver.find_element(By.CSS_SELECTOR, locator_used.password_empty)
        self.assertIn(data_used.password_empty, password_empty.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.confpass_empty)))
        confpass_wrong = driver.find_element(By.CSS_SELECTOR, locator_used.confpass_empty)
        self.assertIn(data_used.confpass_mismatch_message, confpass_wrong.get_attribute("innerText"))

    def test_f_empty_field_confpass(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.new_email)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.confpass_empty)))
        confpass_empty = driver.find_element(By.CSS_SELECTOR, locator_used.confpass_empty)
        self.assertIn(data_used.confpass_empty, confpass_empty.get_attribute("innerText"))

    def test_a_email_exists_already(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_used)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.email_exists)))
        email_exists = driver.find_element(By.CSS_SELECTOR, locator_used.email_exists)
        self.assertIn(data_used.email_exists, email_exists.get_attribute("innerText"))

    def test_b_invalid_email_format(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_wrong)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.email_empty)))
        email_invalid = driver.find_element(By.CSS_SELECTOR, locator_used.email_empty)
        self.assertIn(data_used.email_wrong_message, email_invalid.get_attribute("innerText"))

    def test_a_pass_less_than_six(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.new_email)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password_less)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password_less)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.password_empty)))
        password_less = driver.find_element(By.CSS_SELECTOR, locator_used.password_empty)
        self.assertIn(data_used.password_less_message, password_less.get_attribute("innerText"))

    def test_b_pass_mismatch(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.new_email)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.confpass_mismatch)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.confpass_mismatch)))
        confpass_mismatch = driver.find_element(By.CSS_SELECTOR, locator_used.confpass_mismatch)
        self.assertIn(data_used.confpass_mismatch_message, confpass_mismatch.get_attribute("innerText"))

    def test_a_success_all(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.register_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/register"))

        driver.find_element(By.CSS_SELECTOR, locator_used.radio_female).click()
        driver.find_element(By.CSS_SELECTOR, locator_used.firstname).send_keys(data_used.firstname)
        driver.find_element(By.CSS_SELECTOR, locator_used.lastname).send_keys(data_used.lastname)
        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.new_email)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.conf_pass).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.register_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.success_register)))
        message = driver.find_element(By.CSS_SELECTOR, locator_used.success_register)
        self.assertIn(data_used.success_register, message.get_attribute("innerText"))
        driver.find_element(By.CSS_SELECTOR, locator_used.logout_menu).click()

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()