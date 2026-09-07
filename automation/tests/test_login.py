from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(driver):
    """Test valid login scenario on OrangeHRM with Admin credentials."""
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Perform login using demo credentials
    login_page.login("Admin", "admin123")

    # Verify successful redirection to Dashboard
    assert dashboard_page.is_dashboard_displayed(), "Dashboard was not displayed after valid login."
