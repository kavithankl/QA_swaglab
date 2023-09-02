import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "standard_user"
    password = "secret_sauce"
    wrong_user_name = "Standard"
    wrong_password = "secret"
    first_name = "standard"
    last_name = "user"
    zip_code = "M2R3P4"
    return [user_name, password, wrong_user_name, wrong_password, first_name, last_name, zip_code]


'''@pytest.fixture(scope="function")
def personal_info():
    first_name = "kavitha"
    last_name = "subramani"
    zip_code = "M2R 3P4"
    return [first_name, last_name, zip_code]'''


@pytest.fixture(scope="module")
def driver():
   # _driver = webdriver.Chrome()
    _driver = webdriver.Firefox()
    yield _driver
    _driver.quit()
