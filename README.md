# OrangeHRM QA Assignment

## Overview

This project contains manual and automated QA testing for the OrangeHRM web application.

The assignment covers login functionality, employee management, bug identification, and Selenium automation using the Page Object Model (POM).

## Application Under Test

OrangeHRM Demo Application:

https://opensource-demo.orangehrmlive.com/

## Testing Scope

### Manual Testing

The manual testing covers:

- Valid login
- Invalid username
- Invalid password
- Invalid username and password
- Empty username
- Empty password
- Empty username and password
- Password masking
- Login using the Enter key
- Username with leading/trailing spaces
- Viewing newly added employees
- Updating employees
- Deleting employees

Potential login-page usability issues are also documented.

### Automated Testing

The automated tests cover:

1. Login using valid credentials
2. Verify successful navigation to the Dashboard
3. Hover over the PIM menu and click it
4. Navigate to Add Employee
5. Add four unique employees
6. Navigate to Employee List
7. Search for each created employee
8. Verify that each employee is displayed
9. Print `Name Verified` for each employee
10. Log out from the application

## Technologies Used

- Python 3.11
- Selenium WebDriver
- Pytest
- Chrome WebDriver
- Page Object Model (POM)
- Git and GitHub

## Project Structure

```text
OrangeHRM_QA_Assignment/
│
├── automation/
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── dashboard_page.py
│   │   ├── login_page.py
│   │   └── pim_page.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_employees.py
│   │   └── test_login.py
│   │
│   ├── conftest.py
│   ├── requirements.txt
│   └── README.md
│
├── manual_testing/
│   └── OrangeHRM_Manual_Test_Cases.xlsx
│
├── .gitignore
└── README.md
```

## Page Object Model

The automation follows the Page Object Model design pattern.

### LoginPage

Handles:

- Username input
- Password input
- Login button
- Login operation

File:

`automation/pages/login_page.py`

### DashboardPage

Handles:

- Dashboard verification
- PIM navigation
- Hovering over the PIM menu
- Logout

File:

`automation/pages/dashboard_page.py`

### PIMPage

Handles:

- Add Employee
- Employee List
- Employee search
- Employee verification
- Search reset
- Loading synchronization

File:

`automation/pages/pim_page.py`

## Synchronization

The automation uses Selenium `WebDriverWait` and expected conditions instead of relying on fixed delays.

This improves test reliability when the OrangeHRM application takes time to load or update employee records.

## Running the Automated Tests

### 1. Navigate to the automation directory

```powershell
cd automation
```

### 2. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the tests

```powershell
pytest tests/ -v -s
```

## Test Results

The latest automation execution completed successfully.

```text
2 passed
```

Employee verification output:

```text
Name Verified: QA_First_fc5a7b QA_Last_1
Name Verified: QA_First_93b8ba QA_Last_2
Name Verified: QA_First_5ee466 QA_Last_3
Name Verified: QA_First_bf7017 QA_Last_4
```

The automated test suite contains:

- 1 login automation test
- 1 employee management automation test

Both tests passed successfully.

## Manual Test Documentation

Manual test cases and potential login-page usability issues are documented in:

`manual_testing/OrangeHRM_Manual_Test_Cases.xlsx`

The workbook contains:

- Login test cases
- Employee management test cases
- Login-page usability issues

## Test Data

The employee automation generates unique employee names during execution using UUID-based values.

Example:

```text
QA_First_fc5a7b QA_Last_1
QA_First_93b8ba QA_Last_2
QA_First_5ee466 QA_Last_3
QA_First_bf7017 QA_Last_4
```

This prevents conflicts with previously created employees.

## GitHub Repository

Source code and test documentation are available in this repository:

https://github.com/phaneendra4791/OrangeHRM-QA-Assignment

## Author

Phaneendra Kaveti