import time
import allure
import pytest
from allure_commons.types import AttachmentType
from Utilities.readProperties import ReadConfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.Search_User_Page import Search_User_Class


class Test_Search_User_params:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_search_user_params_005(self, setup, getDataForSearchUser):
        driver = setup
        login_page = Login_Class(driver)
        search_user_page = Search_User_Class(driver)

        # Login steps
        login_page.Click_Login_Link()
        login_page.Enter_Username(self.Username)
        login_page.Enter_Password(self.Password)
        login_page.Click_Login_Button()

        # Search User steps
        search_user_page.Click_Link_User_Management()
        search_username, expected_result = getDataForSearchUser

        search_user_page.Enter_UserName(search_username)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        search_user_page.Click_Search_User_Button()

        # Validation and Allure Reporting
        actual_result = search_user_page.Validate_Search_User()
        is_test_passed = (actual_result == expected_result)

        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert is_test_passed, f"Expected {expected_result} but got {actual_result}"
