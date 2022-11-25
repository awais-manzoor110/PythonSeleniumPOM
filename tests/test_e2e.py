from time import sleep
from utilites.baseclass import BaseClass
from pageObjects.Homepage import Homepage


# Inherit the Baseclass to child class
class Testone(BaseClass):
    def test_e2e(self):
        homepage = Homepage(self.driver)
        # Next page variable initialization
        checkout_page = homepage.shop_items()
        products = checkout_page.select_products()

        for product in products:
            product_name = product.text
            if product_name == "Blackberry":
                checkout_page.selected_one().click()

        checkout_page.button_click().click()
        # Next page variable initialization
        search = checkout_page.success()
        search.search_country().send_keys("pak")
        self.verify_link_presence("Pakistan")
        search.selected_country().click()
        search.checkbox_check().click()
        search.submit_check().click()
        success_text = search.success_message().text
        sleep(3)
        assert "Success! Thank you!" in success_text
