from pages.base_page import BasePage
from pages.checkout_final_info_locators import CheckOutInfoLocators
from resources.constents import MAX_WAIT_INTERVAL


class CheckOutFinalInfo(BasePage):
    def get_payment_info(self):
        payment_info = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutInfoLocators.SUMMERY)
        payment_info_text = payment_info.text
        return payment_info_text

    def click_finish_btn(self):
        finish_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutInfoLocators.FINISH)
        finish_btn.click()
        return finish_btn

    ''' def get_check_out_lbl(self):
        check_out_lbl__txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, CheckOutCompleteLocators.CHECK_OUT_TEXT_LBL).text
        return check_out_lbl__txt'''
