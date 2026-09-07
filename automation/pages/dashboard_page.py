from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    """Page Object for OrangeHRM Dashboard Page."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        # Locators
        self.dashboard_header = (By.XPATH, "//h6[normalize-space()='Dashboard']")
        self.pim_menu_link = (By.XPATH, "//a[contains(@href, 'viewPimModule')]")
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")

    def is_dashboard_displayed(self) -> bool:
        """Verify that the Dashboard page is displayed."""
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.dashboard_header)
            )
            return element.is_displayed()
        except Exception:
            return False

    def get_header_text(self) -> str:
        """Return the header text on the dashboard."""
        element = self.wait.until(
            EC.visibility_of_element_located(self.dashboard_header)
        )
        return element.text

    def navigate_to_pim(self):
        """Hover over the PIM menu and click it."""
        from selenium.webdriver.common.action_chains import ActionChains

        pim_link = self.wait.until(
            EC.visibility_of_element_located(self.pim_menu_link)
        )

        ActionChains(self.driver).move_to_element(pim_link).pause(0.5).click().perform()

    def logout(self):
        """Log out of the application using the user dropdown menu."""
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.user_dropdown)
        )
        dropdown.click()
        logout_item = self.wait.until(
            EC.element_to_be_clickable(self.logout_link)
        )
        logout_item.click()
