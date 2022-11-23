import pytest

from pageObjects.Homepage import Homepage
from testData.Homepagedata import Homepagedata
from utilites.baseclass import BaseClass


class Testhomepage(BaseClass):
    def test_fill_form(self, getdata):
        home_page = Homepage(self.driver)
        home_page.name_ip().send_keys(getdata["Fname"])
        home_page.email_ip().send_keys(getdata["Lname"])
        home_page.checkbox_ip().click()
        self.selectoptionbytext(home_page.gender_ip(), getdata["Gender"])
        home_page.submit_ip().click()
        self.driver.refresh()

    @pytest.fixture(params=Homepagedata.homepage_test_data)
    def getdata(self, request):
        return request.param
