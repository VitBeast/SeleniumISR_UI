from .base_page import Base_Page

from .locators import LoginPageLocators

class LoginPage(Base_Page):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('vkatryuk@yandex.ru')

    def go_to_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('229922vint')

    def go_to_button_click(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
