from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckOutPageLocators(BasePage):
    CHECKOUT_SUCCESS = (By.XPATH, "//div[text()='Checkout: Your Information']")
    FORM = (By.ID, "checkout_info_container")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    # checkoud add again
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ADD_CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CHECK_OUT_BTN = (By.XPATH, "//button[@id='checkout']")