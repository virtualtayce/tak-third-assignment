import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.data import data_used
from pageObject.locator import locator_used

class checkout_cases(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com"

    def test_a_success_checkout(self):
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

        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_used.laptop_name)))
        laptop_name = driver.find_element(By.CSS_SELECTOR, locator_used.laptop_name)
        self.assertIn(data_used.laptop_name, laptop_name.get_attribute("innerText"))
        driver.find_element(By.CSS_SELECTOR, locator_used.laptop_name).click()

        laptop = driver.find_element(By.CSS_SELECTOR, locator_used.laptop_detail)
        self.assertIn(data_used.laptop_name, laptop.get_attribute("innerText"))
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/141-inch-laptop"))

        driver.find_element(By.CSS_SELECTOR, locator_used.quantity).clear()
        driver.find_element(By.CSS_SELECTOR, locator_used.quantity).send_keys(data_used.quantity)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='add-to-cart-button-31']")))
        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button-31']").click()

        driver.find_element(By.ID, 'bar-notification')
        driver.find_element(By.CSS_SELECTOR, locator_used.cart_inside).click()
        get_url = driver.current_url
        self.assertEqual(get_url, str(self.url + "/cart"))

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()