from pages.base_page import BasePage
from pages.checkout_complete_locators import CheckOutCompleteLocators
from resources.constents import MAX_WAIT_INTERVAL


class CheckoutCompletePage(BasePage):

    def get_complete_page(self):
        complete_info = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutCompleteLocators.COMPLETE_MSG)
        complete_info_text = complete_info.text
        return complete_info_text

    def get_again_shop(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              CheckOutCompleteLocators.BACK_HOME).click()
        item_page = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutCompleteLocators.PRODUCT)

        return item_page.text
