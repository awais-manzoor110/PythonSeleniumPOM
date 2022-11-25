from selenium.webdriver.common.by import By


class Confirm:
    def __init__(self, driver):
        self.driver = driver

    search_countries = (By.ID, "country")
    selected = (By.LINK_TEXT, "Pakistan")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def search_country(self):
        return self.driver.find_element(*Confirm.search_countries)

    def selected_country(self):
        return self.driver.find_element(*Confirm.selected)

    def checkbox_check(self):
        return self.driver.find_element(*Confirm.checkbox)

    def submit_check(self):
        return self.driver.find_element(*Confirm.submit)

    def success_message(self):
        return self.driver.find_element(*Confirm.message)
