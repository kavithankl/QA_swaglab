from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginSuccessPageLocators(BasePage):
    LOGIN_SUCCESS_TEXT = (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
    PRODUCT = (By.XPATH, "//*[@id='header_container']/div[2]/span")
    DROP_DOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    FIRST_ITEM_TEXT = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")
    BUTTON_ID = (By.ID, "add-to-cart-sauce-labs-onesie")
    REMOVE_BTN_ID = (By.ID, "remove-sauce-labs-onesie")
    ITEM_NAME_ONE = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ITEM_NAME = (By.CSS_SELECTOR, "#item_2_title_link:nth-child(1) div.inventory_item_name")
    DISPLAY_FIRST_ITEM = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")
    ITEM_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    REMOVE_BTN_TEXT = (By.XPATH, "//button[text()='Remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    MULTIPLE_CART = (By.XPATH, "//button[contains(text(), 'ADD TO CART')]")
    ITEM_NAMES = (By.XPATH, "//div[@class='inventory_item_name']")
