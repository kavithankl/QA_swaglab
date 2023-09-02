import time

from pages.base_page import BasePage
from pages.check_out_page_locators import CheckOutPageLocators
from resources.constents import MAX_WAIT_INTERVAL


class CheckOutPage(BasePage):
    def checkout_success_text(self):
        info = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocators.CHECKOUT_SUCCESS)
        info_text = info.text
        return info_text

    def type_first_name(self, usr_and_pw):
        """self.find_element(CheckOutPageLocators.FIRST_NAME).send_keys(
            usr_and_pw[4])"""
        '''self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocators.FORM)'''
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocators.FIRST_NAME).send_keys(
            usr_and_pw[4])

    def type_last_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocators.LAST_NAME).send_keys(
            usr_and_pw[5])

    def type_zip_code(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocators.ZIP_CODE).send_keys(
            usr_and_pw[6])

    def click_continue_btn(self):
        self.find_element(CheckOutPageLocators.CONTINUE_BUTTON).click()


