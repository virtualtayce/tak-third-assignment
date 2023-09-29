import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.data import data_used
from pageObject.locator import locator_used

class login_cases(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com"

    def test_a_empty_field_all(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.login_wrong)))
        login_wrong = driver.find_element(By.CSS_SELECTOR, locator_used.login_wrong)
        self.assertIn(data_used.login_wrong_message, login_wrong.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.no_account)))
        no_account = driver.find_element(By.CSS_SELECTOR, locator_used.no_account)
        self.assertIn(data_used.no_account, no_account.get_attribute("innerText"))
    
    def test_b_empty_field_email(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.login_wrong)))
        login_wrong = driver.find_element(By.CSS_SELECTOR, locator_used.login_wrong)
        self.assertIn(data_used.login_wrong_message, login_wrong.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.no_account)))
        no_account = driver.find_element(By.CSS_SELECTOR, locator_used.no_account)
        self.assertIn(data_used.no_account, no_account.get_attribute("innerText"))

    def test_c_empty_field_pass(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_used)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.field_empty)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.login_wrong)))
        login_wrong = driver.find_element(By.CSS_SELECTOR, locator_used.login_wrong)
        self.assertIn(data_used.login_wrong_message, login_wrong.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.no_account)))
        wrong_cred = driver.find_element(By.CSS_SELECTOR, locator_used.no_account)
        self.assertIn(data_used.wrong_cred, wrong_cred.get_attribute("innerText"))

    def test_a_email_mismatch(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.new_email)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.login_wrong)))
        login_wrong = driver.find_element(By.CSS_SELECTOR, locator_used.login_wrong)
        self.assertIn(data_used.login_wrong_message, login_wrong.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.no_account)))
        no_account = driver.find_element(By.CSS_SELECTOR, locator_used.no_account)
        self.assertIn(data_used.no_account, no_account.get_attribute("innerText"))

    def test_b_invalid_email_format(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_wrong)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.confpass_mismatch)))
        invalid_email = driver.find_element(By.CSS_SELECTOR, locator_used.confpass_mismatch)
        self.assertIn(data_used.email_inv_message, invalid_email.get_attribute("innerText"))

    def test_a_pass_mismatch(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_used)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password_less)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.login_wrong)))
        login_wrong = driver.find_element(By.CSS_SELECTOR, locator_used.login_wrong)
        self.assertIn(data_used.login_wrong_message, login_wrong.get_attribute("innerText"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.no_account)))
        wrong_cred = driver.find_element(By.CSS_SELECTOR, locator_used.no_account)
        self.assertIn(data_used.wrong_cred, wrong_cred.get_attribute("innerText"))

    def test_a_success_login(self):
        driver = self.browser
        driver.get(self.url)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, locator_used.login_menu).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/login"))

        driver.find_element(By.CSS_SELECTOR, locator_used.email).send_keys(data_used.email_used)
        driver.find_element(By.CSS_SELECTOR, locator_used.password).send_keys(data_used.password)
        driver.find_element(By.CSS_SELECTOR, locator_used.login_button).click()

        get_url = driver.current_url
        self.assertEqual(get_url, str("https://demowebshop.tricentis.com/"))

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.email_menu)))
        email_menu = driver.find_element(By.CSS_SELECTOR, locator_used.email_menu)
        self.assertIn(data_used.email_used, email_menu.get_attribute("innerText"))

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()