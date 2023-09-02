from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckOutInfoLocators(BasePage):
    SUMMERY = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[2]")
    FINISH = (By.ID, "finish")
