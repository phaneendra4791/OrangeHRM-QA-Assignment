from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException


class PIMPage:
    """Page Object for OrangeHRM PIM Module Page."""

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        # Locators
        self.add_employee_tab = (By.XPATH, "//a[text()='Add Employee']")
        self.employee_list_tab = (By.XPATH, "//a[text()='Employee List']")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.save_success_indicator = (
            By.XPATH,
            "//h6[text()='Personal Details'] | //div[contains(@class, 'oxd-toast-content')]",
        )
        self.search_name_input = (
            By.XPATH,
            "//label[text()='Employee Name']/parent::div/following-sibling::div//input",
        )
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.reset_button = (By.XPATH, "//button[normalize-space()='Reset']")
        self.loading_spinner = (
            By.XPATH,
            "//div[contains(@class, 'oxd-loading-spinner') or contains(@class, 'oxd-form-loader') or contains(@class, 'oxd-table-loader')]",
        )

    def wait_for_loading(self, timeout=15):
        """Wait for any loading spinner or loader overlay to disappear."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(self.loading_spinner)
            )
        except Exception:
            pass

    def safe_click(self, locator, timeout=15):
        """Safely click an element, handling potential loader overlays."""
        self.wait_for_loading(timeout)
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.wait_for_loading(timeout)
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    def click_add_employee_tab(self):
        """Click the Add Employee tab in PIM header menu."""
        self.safe_click(self.add_employee_tab)

    def click_employee_list_tab(self):
        """Click the Employee List tab in PIM header menu."""
        self.safe_click(self.employee_list_tab)

    def add_employee(self, first_name: str, last_name: str):
        """Fill and submit the Add Employee form."""
        self.wait_for_loading()
        fname_el = self.wait.until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        fname_el.clear()
        fname_el.send_keys(first_name)

        lname_el = self.wait.until(
            EC.visibility_of_element_located(self.last_name_input)
        )
        lname_el.clear()
        lname_el.send_keys(last_name)

        self.safe_click(self.save_button)

        # Wait until save operation completes
        self.wait.until(
            EC.presence_of_element_located(self.save_success_indicator)
        )
        self.wait_for_loading()

    def search_employee(self, first_name: str):
        """Search for an employee by first name in the Employee List filter."""
        self.wait_for_loading()
        name_input = self.wait.until(
            EC.visibility_of_element_located(self.search_name_input)
        )
        name_input.clear()
        name_input.send_keys(first_name)

        self.safe_click(self.search_button)

        # Wait for search results loader to finish
        self.wait_for_loading()

    def is_employee_in_list(self, first_name: str) -> bool:
        """Verify if an employee with the given first_name exists in search results after table update."""
        self.wait_for_loading()
        cell_locator = (
            By.XPATH,
            f"//div[@role='table' or contains(@class, 'orangehrm-container')]//div[contains(text(), '{first_name}')]",
        )
        try:
            cell = self.wait.until(
                EC.visibility_of_element_located(cell_locator)
            )
            return cell.is_displayed()
        except Exception:
            return False

    def reset_search_filter(self):
        """Reset search filters on the Employee List page."""
        try:
            self.safe_click(self.reset_button)
            self.wait_for_loading()
            self.wait.until(EC.element_to_be_clickable(self.search_button))
        except Exception:
            pass
