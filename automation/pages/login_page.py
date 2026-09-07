from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object for OrangeHRM Login Page."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        # Locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username: str):
        """Enter username into the username input field."""
        user_element = self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        )
        user_element.clear()
        user_element.send_keys(username)

    def enter_password(self, password: str):
        """Enter password into the password input field."""
        pass_element = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )
        pass_element.clear()
        pass_element.send_keys(password)

    def click_login(self):
        """Click the login submit button."""
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_btn.click()

    def login(self, username: str, password: str):
        """Perform full login action with username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
