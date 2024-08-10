from selenium.webdriver.common.by import By


class Search_User_Class:

    click_link_user_management_xpath = "//a[normalize-space()='User Management']"
    text_username_xpath = "//input[@id='username']"
    click_search_user_button_xpath = "//button[@type='submit']"
    Validate_search_user_page_title_css = "div[class='container'] h2"



    def __init__(self, driver):
        self.driver = driver


    def Click_Link_User_Management(self):
        self.driver.find_element(By.XPATH, self.click_link_user_management_xpath).click()

    def Enter_UserName(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def Click_Search_User_Button(self):
        self.driver.find_element(By.XPATH, self.click_search_user_button_xpath).click()

    def Validate_Search_User(self):
        title = self.driver.find_element(By.CSS_SELECTOR, self.Validate_search_user_page_title_css).text
        if title == "Edit User":
            return "pass"
        else:
            return "fail"










