from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogOutPageLocators(BasePage):
    LOG_OUT_LINK = (By.ID, "logout_sidebar_link")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
