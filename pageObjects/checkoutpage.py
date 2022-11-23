from selenium.webdriver.common.by import By

from pageObjects.confirmpage import Confirm


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    selected_product = (By.XPATH, "div/button")
    btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    success_btn = (By.XPATH, "//button[@class='btn btn-success']")

    def select_products(self):
        return self.driver.find_elements(*Checkout.products)

    def selected_one(self):
        return self.driver.find_element(*Checkout.selected_product)

    def button_click(self):
        return self.driver.find_element(*Checkout.btn)

    def success(self):
        self.driver.find_element(*Checkout.success_btn).click()

        # Next page object creation
        search = Confirm(self.driver)
        return search
