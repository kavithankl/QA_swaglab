from test_utils import *
import time

from pages.add_cart_page import AddCartSuccessPage
from pages.check_out_page import CheckOutPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_final_info_page import CheckOutFinalInfo
from pages.index_page import IndexPage
from pages.login_success_page import LoginSuccessPage
from resources.constents import TEST_SITE_URL
from pages.logout_page import LogOutPage


class TestLogin:

    # Test Case ( Successful login and unsuccessful login)
    def test_login_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
        # Invalid username and valid Password
        login_page.wrong_and_type_user_name(username_password)
        login_page.type_password(username_password)
        time.sleep(5)
        login_page.click_submit_btn()
        login_failed = login_page.error_message()
        login_failed_text = "Epic sadface: Username and password do not match any user in this service"
        print(login_failed_text)
        assert login_failed == login_failed_text, "login failed"
        login_page.error_button_click()
        time.sleep(3)
        login_page.user_clear()
        time.sleep(2)
        # valid username and Invalid Password
        login_page.wait_and_type_user_name(username_password)
        login_page.pass_clear()
        login_page.wrong_and_type_password(username_password)
        login_page.click_submit_btn()
        login_failed = login_page.error_message()
        login_failed_text = "Epic sadface: Username and password do not match any user in this service"
        print(login_failed_text)
        login_page.error_button_click()
        time.sleep(3)
        assert login_failed == login_failed_text, "login failed"
        login_page.user_clear()
        # Successful Login
        time.sleep(2)
        login_page.wait_and_type_user_name(username_password)
        time.sleep(2)
        login_page.pass_clear()
        login_page.type_password(username_password)
        login_page.click_submit_btn()

    def test_inventory_page(self, driver):
        login_success_page = LoginSuccessPage(driver)
        time.sleep(2)
        login_success_lbl = login_success_page.get_login_success_label()
        login_success_lbl_text = "Products"
        print(login_success_lbl_text)
        assert login_success_lbl == login_success_lbl_text, "User Login failed!"

        display_item = login_success_page.display_item_page()
        display_item_text = "Sauce Labs Backpack"
        assert display_item == display_item_text, "Item not displayed on the page"

        select_option = login_success_page.filter_option()
        expected_option_text = "Sauce Labs Onesie"
        assert select_option == expected_option_text, " first item not found"
        add_cart_btn = login_success_page.add_cart()
        item_count = 1
        assert add_cart_btn == item_count, "Item not added to the cart "

        login_success_page.add_cart_link_click()

    def test_checkout(self, driver, username_password):
        cart_success_page = AddCartSuccessPage(driver)
        page_title = cart_success_page.verify_page_title()
        page_title_text = "Your Cart"
        assert page_title == page_title_text, "Page information  not display "

        display_add_cart_item = cart_success_page.item_display()
        item_name = "Sauce Labs Onesie"
        assert display_add_cart_item == item_name, "Add to cart item not display correctly"

        '''remove_item = cart_success_page.item_remove()
        item_count = 1
        assert remove_item == item_count, "Item not removed successfully"'''
        cart_success_page.click_checkout()

    def test_checkout_item(self, driver, username_password):
        checkout_success_page = CheckOutPage(driver)
        ''' checkout_success = checkout_success_page.checkout_success_text()
        checkout_success_name = checkout_success.text
        checkout_success_text = "Checkout: Your Information"
        assert checkout_success_name == checkout_success_text, "Your information page not displayed"'''

        checkout_success_page.type_first_name(username_password)
        time.sleep(2)
        checkout_success_page.type_last_name(username_password)
        checkout_success_page.type_zip_code(username_password)
        time.sleep(5)
        checkout_success_page.click_continue_btn()
        checkout_final_information = CheckOutFinalInfo(driver)
        summery = checkout_final_information.get_payment_info()
        payment_info = "SauceCard #31337"
        assert summery == payment_info, "card information not displayed"
        time.sleep(5)
        checkout_final_information.click_finish_btn()
        checkout_complete = CheckoutCompletePage(driver)

        checkout_complete_text = checkout_complete.get_complete_page()
        expected_complete_text = "Thank you for your order!"
        assert checkout_complete_text == expected_complete_text, "checkout process not complete"

        back_shop = checkout_complete.get_again_shop()
        inventory_page = "Products"
        assert back_shop == inventory_page, "not successfully navigate the item page"

    def test_logout(self, driver):
        logout_page = LogOutPage(driver)
        time.sleep(5)
        logout_page.click_menu_btn()
        time.sleep(5)
        assert "https://www.saucedemo.com/" == TEST_SITE_URL, " Logout not successfully"
