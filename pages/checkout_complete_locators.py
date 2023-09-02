from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckOutCompleteLocators(BasePage):
    COMPLETE_MSG = (By.TAG_NAME, "h2")
    BACK_HOME = (By.ID, "back-to-products")
    PRODUCT = (By.XPATH, "//*[@id='header_container']/div[2]/span")
    # CHECK_OUT_TEXT_LBL = (By.XPATH, "//h2[@class='complete-header']")
