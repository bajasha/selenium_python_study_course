from .base_page import BasePage
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_FORM), "Login Form is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.browser.find_element(*BasePageLocators.REGISTER_FORM), "Registration Form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*BasePageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.REGISTER_PASS1).send_keys(password)
        self.browser.find_element(*BasePageLocators.REGISTER_PASS2).send_keys(password)
        self.browser.find_element(*BasePageLocators.REGISTER_SUBMIT).click()



