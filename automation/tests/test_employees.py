import uuid
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


def test_add_and_verify_employees(driver):
    """Test adding 4 unique employees, verifying them in Employee List, and logging out."""
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    pim_page = PIMPage(driver)

    # 1. Login
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_displayed(), "Failed to reach Dashboard."

    # 2. Navigate to PIM module
    dashboard_page.navigate_to_pim()

    # 3. Add 4 employees with unique names
    created_employees = []
    for i in range(1, 5):
        pim_page.click_add_employee_tab()
        
        unique_suffix = uuid.uuid4().hex[:6]
        first_name = f"QA_First_{unique_suffix}"
        last_name = f"QA_Last_{i}"
        
        pim_page.add_employee(first_name, last_name)
        created_employees.append((first_name, last_name))

    # 4. Navigate to Employee List and verify all 4 created employees
    pim_page.click_employee_list_tab()

    for first_name, last_name in created_employees:
        full_name = f"{first_name} {last_name}"
        
        # Search for employee by unique first name
        pim_page.search_employee(first_name)
        
        # Verify employee is listed
        found = pim_page.is_employee_in_list(first_name)
        assert found, f"Employee '{full_name}' was not found in Employee List."
        
        # Print verification line required by specification
        print(f"Name Verified: {full_name}")
        
        # Reset filter for next search
        pim_page.reset_search_filter()

    # 5. Log out
    dashboard_page.logout()
