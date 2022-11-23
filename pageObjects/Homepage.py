from selenium.webdriver.common.by import By

from pageObjects.checkoutpage import Checkout


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "/html/body/app-root/form-comp/div/form/input")

    def shop_items(self):
        self.driver.find_element(*Homepage.shop).click()
        # Next page object creation
        checkout_page = Checkout(self.driver)
        return checkout_page

    def name_ip(self):
        return self.driver.find_element(*Homepage.name)

    def email_ip(self):
        return self.driver.find_element(*Homepage.email)

    def checkbox_ip(self):
        return self.driver.find_element(*Homepage.checkbox)

    def gender_ip(self):
        return self.driver.find_element(*Homepage.gender)

    def submit_ip(self):
        return self.driver.find_element(*Homepage.submit)
