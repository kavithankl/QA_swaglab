import time

from pages.base_page import BasePage
from pages.checkout_complete_locators import CheckOutCompleteLocators
from pages.login_success_page_locators import LoginSuccessPageLocators
from pages.logout_page_Locators import LogOutPageLocators
from resources.constents import MAX_WAIT_INTERVAL


class LogOutPage(BasePage):

    def click_menu_btn(self):
        menu_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LogOutPageLocators.MENU_BTN)
        menu_btn.click()
        time.sleep(3)

        log_out = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LogOutPageLocators.LOG_OUT_LINK)
        log_out.click()
        time.sleep(3)
