import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# use the setup method at base class
@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_presence(self, text):
        # Explicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoptionbytext(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
